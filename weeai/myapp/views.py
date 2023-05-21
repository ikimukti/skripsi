from datetime import datetime
import hashlib
import os
import cv2 as cv
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
import numpy as np
from .models import XImage, XSegmentationResult
from django.utils.text import slugify
from .forms import ImageUploadForm
from django.db.models import OuterRef, Subquery, Q
from django.core.paginator import Paginator
import sweetify
from django.contrib import messages
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, rand_score, jaccard_score, mean_squared_error, mean_absolute_error


menus = [
    {'name': 'Dashboard', 'url': '/dashboard/', 'icon': 'fas fa-tachometer-alt', 'id': 'dashboard'},
    
    {'name': 'Account', 'url': '/account/', 'icon': 'fas fa-user', 'dropdown': True, 'id': 'account'
    ,'submenus': [
        {'name': 'Profile', 'url': '/account/profile/', 'icon': 'fas fa-user-circle', 'id': 'accountProfile'},
        {'name': 'Change Password', 'url': '/account/change-password/', 'icon': 'fas fa-key', 'id': 'accountChangePassword'},
    ]},
    {'name': 'Images', 'url': '/image/', 'icon': 'fas fa-image', 'dropdown': True, 'id': 'image'
    ,'submenus': [
        {'name': 'List', 'url': '/image/list/', 'icon': 'fas fa-list', 'id': 'imageList'},
        {'name': 'Upload', 'url': '/image/upload/', 'icon': 'fas fa-upload', 'id': 'imageUpload'},
        {'name': 'Summary', 'url': '/image/summary/', 'icon': 'fas fa-chart-bar', 'id': 'imageSummary'},
        {'name': 'Manage', 'url': '/image/manage/', 'icon': 'fas fa-cog', 'id': 'imageManage'},
    ]},
    # submenus manage
    {'name': 'Manage', 'url': '/manage/', 'icon': 'fas fa-cogs', 'dropdown': True, 'id': 'manage'
    ,'submenus': [
        {'name': 'User', 'url': '/manage/user/', 'icon': 'fas fa-user', 'id': 'manageUser'},
        {'name': 'Role', 'url': '/manage/role/', 'icon': 'fas fa-user-tag', 'id': 'manageRole'},
        {'name': 'Permission', 'url': '/manage/permission/', 'icon': 'fas fa-user-lock', 'id': 'managePermission'},
        {'name': 'Group', 'url': '/manage/group/', 'icon': 'fas fa-users', 'id': 'manageGroup'},
    ]},
    {'name': 'Reports', 'url': '/report/', 'icon': 'fas fa-chart-bar', 'dropdown': True, 'id': 'report'
    ,'submenus': [
        {'name': 'Segmentation', 'url': '/report/segmentation/', 'icon': 'fas fa-chart-pie', 'id': 'reportSegmentation'},
        {'name': 'Export Image', 'url': '/report/export/image/', 'icon': 'fas fa-file-image', 'id': 'reportExportImage'},
        {'name': 'Export Report', 'url': '/report/export/report/', 'icon': 'fas fa-file-pdf', 'id': 'reportExportReport'},
        {'name': 'Summary', 'url': '/report/summary/', 'icon': 'fas fa-chart-bar', 'id': 'reportSummary'},
    ]},
    {'name': 'Preferences', 'url': '/preference/', 'icon': 'fas fa-cog', 'dropdown': True, 'id': 'preference'
    ,'submenus': [
        {'name': 'Setting', 'url': '/preference/setting/', 'icon': 'fas fa-cog', 'id': 'preferenceSetting'},
        {'name': 'Help', 'url': '/help/', 'icon': 'fas fa-question-circle', 'id': 'preferenceHelp'},
        {'name': 'Docs', 'url': '/docs/', 'icon': 'fas fa-book', 'id': 'preferenceDocs'},
        {'name': 'Blog', 'url': '/blog/', 'icon': 'fas fa-blog', 'id': 'preferenceBlog'},
        {'name': 'Contact', 'url': '/contact/', 'icon': 'fas fa-phone', 'id': 'preferenceContact'},
        {'name': 'About', 'url': '/about/', 'icon': 'fas fa-info-circle', 'id': 'preferenceAbout'},
    ]},
]

def calculate_scores(ground_truth, segmented, type):
    scores = {}
    scores['f1'] = str(round(f1_score(ground_truth.flatten(), segmented.flatten(), average='binary', zero_division=1, labels=[0, 1], sample_weight=None, pos_label=1), 2))
    scores['precision'] = str(round(precision_score(ground_truth.flatten(), segmented.flatten(), average='binary', zero_division=1, labels=[0, 1], sample_weight=None, pos_label=1), 2))
    scores['recall'] = str(round(recall_score(ground_truth.flatten(), segmented.flatten(), average='binary', zero_division=1, labels=[0, 1], sample_weight=None, pos_label=1), 2))
    scores['accuracy'] = str(round(accuracy_score(ground_truth.flatten(), segmented.flatten()), 2))
    scores['rand'] = str(round(rand_score(ground_truth.flatten(), segmented.flatten()), 2))
    scores['jaccard'] = str(round(jaccard_score(ground_truth.flatten(), segmented.flatten(), average='binary', zero_division=1, labels=[0, 1], sample_weight=None, pos_label=1), 2))
    scores['mse'] = str(round(mean_squared_error(ground_truth.flatten(), segmented.flatten()), 2))
    scores['mae'] = str(round(mean_absolute_error(ground_truth.flatten(), segmented.flatten()), 2))
    scores['rmse'] = str(round(mean_squared_error(ground_truth.flatten(), segmented.flatten(), squared=False), 2))
    return scores

def modal(request):
    context = {
        'title': 'Modal',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/snippets/modal.html", context)

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'contributor': 'WeeAI Team',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    print(request.user)
    return render(request, "myapp/index.html", context)

def contact(request):
    context = {
        'title': 'Contact',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/contact.html", context)

def dashboard(request):

    context = {
        'title': 'Dashboard',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    sweetify.success(request, 'Operation successful!', persistent='Dismiss')
    return render(request, "myapp/dashboard.html", context)

def docs(request):
    context = {
        'title': 'Docs',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/docs.html", context)

def blog(request):
    context = {
        'title': 'Blog',
        'contributor': 'WeeAI Team',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'posts': [
            {'title': 'Blog Post 1', 'url': '/blog/post1/', 'content': 'Welcome to WeeAI!','author': 'WeeAI Team','date_posted': 'August 27, 2018'},
            {'title': 'Blog Post 2', 'url': '/blog/post2/', 'content': 'Welcome to WeeAI!','author': 'WeeAI Team','date_posted': 'August 28, 2018'},
            {'title': 'Blog Post 3', 'url': '/blog/post3/', 'content': 'Welcome to WeeAI!','author': 'WeeAI Team','date_posted': 'August 29, 2018'},
        ],
    }
    return render(request, "myapp/blog.html", context)

def setting(request):
    context = {
        'title': 'Setting',
        'contributor': 'WeeAI Team',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/preference/preferenceSetting.html", context)

def help(request):
    context = {
        'title': 'Help',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/help.html", context)

def image(request):
    # Mendapatkan XSegmentationResult terkait jika ada (hanya 1) dan buat field baru xsegmentation_result
    xsegmentation_results = XSegmentationResult.objects.filter(idImage=OuterRef('pk'))
    # Definisikan semua field yang ingin diambil
    fields = [
        'report',
        'id',
        'idImage',
        'pathSegmentationKMeans',
        'pathSegmentationAdaptive',
        'pathGroundTruth',
        'date'
    ]

    # Buat dictionary comprehension untuk mengambil semua field
    xsegmentation_result_fields = {
        f'xsegmentation_result_{field}': Subquery(xsegmentation_results.values(field)[:1])
        for field in fields
    }

    # Search bar untuk pencarian
    if 'q' in request.GET:
        q = request.GET['q']
        # Mendapatkan semua objek XImage yang mengandung q di all field
        # date, id, pathImage, slug, uploader, xsegmentationresult
        ximages = XImage.objects.filter(
            Q(date__icontains=q) | Q(id__icontains=q) | Q(pathImage__icontains=q) | Q(slug__icontains=q) | Q(uploader__icontains=q)
        ).order_by('-date')
    else:
        # Mendapatkan semua objek XImage
        ximages = XImage.objects.all().order_by('-date')
    # Anotasi XImage dengan field-field yang diambil
    ximages = ximages.annotate(**xsegmentation_result_fields)
    # pagination
    paginator = Paginator(ximages, 10)
    page_list = request.GET.get('page')
    ximages = paginator.get_page(page_list)

    context = {
        'title': 'Image',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'images': ximages,
    }
    return render(request, "myapp/image/image.html", context)



def imageUpload(request):
    image_upload_form = ImageUploadForm()

    context = {
        'title': 'Image Upload',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'ImageUploadForm': image_upload_form,
    }
    if request.method == 'POST':
        files = request.FILES.getlist('image')
        # files count
        files_count = len(files)
        # for in range files count
        for count in range(files_count):
            print(count)
            # hash for unique file name and time + extension
            name = hashlib.md5(files[count].name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + os.path.splitext(files[count].name)[1]
            
            # Save the uploaded image
            with open('myapp/static/myapp/images/' + name, 'wb+') as destination:
                for chunk in files[count].chunks():
                    destination.write(chunk)
            img = cv.imread('myapp/static/myapp/images/' + name)
            # Image resizing to maxwidth 500px and keep aspect ratio
            # Get the original image dimensions
            height, width = img.shape[:2]
            # Set the maximum width for resizing
            max_width = 500
            # Get the original image dimensions
            # Calculate the new dimensions while maintaining the aspect ratio
            if width > max_width:
                ratio = max_width / width
                new_width = max_width
                new_height = int(height * ratio)
            else:
                new_width = width
                new_height = height

            # Resize the image using the calculated dimensions
            resized_image = cv.resize(img, (new_width, new_height), interpolation=cv.INTER_AREA)
            cv.imwrite('myapp/static/myapp/images/' + name, resized_image)
            XImage.objects.create(
                pathImage = name,
                uploader = request.POST.get('uploader'),
                slug = name,
                date = datetime.now(),
            )
            img = cv.imread('myapp/static/myapp/images/' + name)
            # Save the resized image
            # Image contrast enhancement
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convert to grayscale
            img = img.astype(np.uint8)  # Convert to 8-bit unsigned integer typ
            img = cv.equalizeHist(img)
            # Convert from BGR to RGB
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            name_rgb = hashlib.md5(files[count].name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + '_rgb' + os.path.splitext(files[count].name)[1]
            cv.imwrite('myapp/static/myapp/images/' + name_rgb, img)
            # conver from RGB to Grayscale
            img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
            name_gray = hashlib.md5(files[count].name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + '_gray' + os.path.splitext(files[count].name)[1]
            cv.imwrite('myapp/static/myapp/images/' + name_gray, img)
            # Convert to float type
            img_2d = img.astype(np.float32)
            # data is not a numpy array, neither a scalar
            img_2d = np.reshape(img_2d, (-1, 1))
            # Apply kmeans
            k = 2
            criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            ret, label, center = cv.kmeans(img_2d, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
            segmented1 = center[label.flatten()]
            segmented1 = segmented1.reshape(img.shape)
            # Apply adaptive threshold
            segmented2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
            # Apply Otsu's thresholding
            ret, segmented3 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
            # Apply Canny edge detection
            edges = cv.Canny(img, 100, 200)
            segmented4 = cv.bitwise_and(img, img, mask=edges)
            # Apply Sobel edge detection
            sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
            sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
            segmented5 = cv.bitwise_or(sobelx, sobely)
            # Apply Prewitt edge detection on img
            kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
            kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
            img_prewittx = cv.filter2D(img, -1, kernelx)
            img_prewitty = cv.filter2D(img, -1, kernely)
            segmented6 = cv.bitwise_or(img_prewittx, img_prewitty)
            
            
            # Save segmented1 image
            name_segmented1 = hashlib.md5(files[count].name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + '_segmented1' + os.path.splitext(files[count].name)[1]
            cv.imwrite('myapp/static/myapp/images/' + name_segmented1, segmented1)
            # Save segmented2 image
            name_segmented2 = hashlib.md5(files[count].name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + '_segmented2' + os.path.splitext(files[count].name)[1]
            cv.imwrite('myapp/static/myapp/images/' + name_segmented2, segmented2)
            # Save segmented3 image
            name_segmented3 = hashlib.md5(files[count].name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + '_segmented3' + os.path.splitext(files[count].name)[1]
            cv.imwrite('myapp/static/myapp/images/' + name_segmented3, segmented3)
            # Save segmented4 image
            name_segmented4 = hashlib.md5(files[count].name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + '_segmented4' + os.path.splitext(files[count].name)[1]
            cv.imwrite('myapp/static/myapp/images/' + name_segmented4, segmented4)
            # Save segmented5 image
            name_segmented5 = hashlib.md5(files[count].name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + '_segmented5' + os.path.splitext(files[count].name)[1]
            cv.imwrite('myapp/static/myapp/images/' + name_segmented5, segmented5)
            # Save segmented6 image
            name_segmented6 = hashlib.md5(files[count].name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + '_segmented6' + os.path.splitext(files[count].name)[1]
            cv.imwrite('myapp/static/myapp/images/' + name_segmented6, segmented6)
            # Save ground truth
            ground_truth = np.zeros_like(img)
            ground_truth = np.reshape(ground_truth, label.shape)
            ground_truth[label.flatten() == 0] = 255
            ground_truth = np.reshape(ground_truth, img.shape)
            # if black area is the background, then invert the image
            if np.sum(ground_truth[0]) > np.sum(ground_truth[-1]):
                ground_truth = cv.bitwise_not(ground_truth)
            name_ground_truth = hashlib.md5(files[count].name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + '_ground_truth' + os.path.splitext(files[count].name)[1]
            cv.imwrite('myapp/static/myapp/images/' + name_ground_truth, ground_truth)
            # convert the image segmented1 and ground truth to binary format (0 or 1)
            ground_truth[ground_truth > 0] = 1
            segmented1[segmented1 > 0] = 1
            segmented2[segmented2 > 0] = 1
            segmented3[segmented3 > 0] = 1
            segmented4[segmented4 > 0] = 1
            segmented5[segmented5 > 0] = 1
            segmented6[segmented6 > 0] = 1
            
            # Calculate scores for segmented1
            scores_kmeans = calculate_scores(ground_truth, segmented1, 'kmeans')

            # Calculate scores for segmented2
            scores_adaptive = calculate_scores(ground_truth, segmented2, 'adaptive')
            
            # Calculate scores for segmented3
            scores_otsu = calculate_scores(ground_truth, segmented3, 'otsu')
            
            # Calculate scores for segmented4
            scores_canny = calculate_scores(ground_truth, segmented4, 'canny')
            
            # Calculate scores for segmented5
            scores_sobel = calculate_scores(ground_truth, segmented5, 'sobel')
            
            # Calculate scores for segmented6
            scores_prewitt = calculate_scores(ground_truth, segmented6, 'prewitt')
            
            # save segmentation result to database
            XSegmentationResult.objects.create(
                pathSegmentationKMeans = name_segmented1,
                pathSegmentationAdaptive = name_segmented2,
                pathSegmentationOtsu = name_segmented3,
                pathGroundTruth = name_ground_truth,
                pathDeteksiTepiCanny = name_segmented4,
                pathDeteksiTepiSobel = name_segmented5,
                pathDeteksiTepiPrewitt = name_segmented6,
                report = {
                    'kmeans': scores_kmeans,
                    'adaptive': scores_adaptive,
                    'otsu': scores_otsu,
                    'canny': scores_canny,
                    'sobel': scores_sobel,
                    'prewitt': scores_prewitt,
                },
                date = datetime.now(),
                idImage_id = XImage.objects.get(pathImage=name).id,
            )
            
    return render(request, "myapp/image/imageUpload.html", context)

def imageSingle(request, id):
    # Mendapatkan XSegmentationResult terkait jika ada (hanya 1) dan buat field baru xsegmentation_result
    xsegmentation_results = XSegmentationResult.objects.filter(idImage=OuterRef('pk'))
    # Definisikan semua field yang ingin diambil
    fields = [
        'report',
        'id',
        'idImage',
        'pathSegmentationKMeans',
        'pathSegmentationAdaptive',
        'pathGroundTruth',
        'date'
    ]

    # Buat dictionary comprehension untuk mengambil semua field
    xsegmentation_result_fields = {
        f'xsegmentation_result_{field}': Subquery(xsegmentation_results.values(field)[:1])
        for field in fields
    }
    image = XImage.objects.annotate(**xsegmentation_result_fields).get(id=id)
    context = {
        'title': 'Image Single',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'image': image,	
    }
    return render(request, "myapp/image/imageSingle.html", context)

def imageUploader(request, uploader):
    
    images = XImage.objects.filter(uploader=uploader)
    context = {
        'title': 'Image Uploader',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'images': images,	
    }
    return render(request, "myapp/image/imageUploader.html", context)

def imageSummary(request):
    images = XImage.objects.all()
    context = {
        'title': 'Image Summary',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'images': images,	
    }
    return render(request, "myapp/image/imageSummary.html", context)

def imageManage(request):
    images = XImage.objects.all()
    context = {
        'title': 'Image Manage',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'images': images,	
    }
    return render(request, "myapp/image/imageManage.html", context)

def imageList(request):
    # Mendapatkan XSegmentationResult terkait jika ada (hanya 1) dan buat field baru xsegmentation_result
    xsegmentation_results = XSegmentationResult.objects.filter(idImage=OuterRef('pk'))
    # Definisikan semua field yang ingin diambil
    fields = [
        'report',
        'id',
        'idImage',
        'pathSegmentationKMeans',
        'pathSegmentationAdaptive',
        'pathGroundTruth',
        'date'
    ]

    # Buat dictionary comprehension untuk mengambil semua field
    xsegmentation_result_fields = {
        f'xsegmentation_result_{field}': Subquery(xsegmentation_results.values(field)[:1])
        for field in fields
    }

    # Search bar untuk pencarian
    if 'q' in request.GET:
        q = request.GET['q']
        # Mendapatkan semua objek XImage yang mengandung q di all field
        # date, id, pathImage, slug, uploader, xsegmentationresult
        ximages = XImage.objects.filter(
            Q(date__icontains=q) | Q(id__icontains=q) | Q(pathImage__icontains=q) | Q(slug__icontains=q) | Q(uploader__icontains=q)
        )
    else:
        # Mendapatkan semua objek XImage
        ximages = XImage.objects.all()
    # Anotasi XImage dengan field-field yang diambil
    ximages = ximages.annotate(**xsegmentation_result_fields)
    # pagination
    paginator = Paginator(ximages, 10)
    page_list = request.GET.get('page')
    ximages = paginator.get_page(page_list)

    context = {
        'title': 'Image List',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'images': ximages,
    }
    return render(request, "myapp/image/imageList.html", context)

def about(request):
    context = {
        'title': 'About',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/about.html", context)

def signin(request):
    context = {
        'title': 'Sign In',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/system/signin.html", context)

def signup(request):
    context = {
        'title': 'Sign Up',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/system/signup.html", context)

def signout(request):
    context = {
        'title': 'Sign Out',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/system/signout.html", context)

def account(request):
    context = {
        'title': 'Account',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/account/account.html", context)

def accountProfile(request):
    context = {
        'title': 'Profile',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/account/profile.html", context)

def accountChangePassword(request):
    context = {
        'title': 'Change Password',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/account.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/account/password.html", context)

def manage(request):
    context = {
        'title': 'Manage',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/manage/manage.html", context)

def manageUser(request):
    context = {
        'title': 'Manage User',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/manage/manageUser.html", context)

def manageRole(request):
    context = {
        'title': 'Manage Role',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/manage/manageRole.html", context)

def managePermission(request):
    context = {
        'title': 'Manage Permission',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/manage/managePermission.html", context)

def manageGroup(request):
    context = {
        'title': 'Manage Group',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/manageGroup.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/manage/manageGroup.html", context)

def report(request):
    context = {
        'title': 'Report',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/report/report.html", context)

def reportSegmentation(request):
    context = {
        'title': 'Segmentation Report',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/report/reportSegmentation.html", context)

def reportExportImage(request):
    context = {
        'title': 'Export Image Report',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/report/reportExportImage.html", context)

def reportExportReport(request):
    context = {
        'title': 'Export Report',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/report/reportExportReport.html", context)

def reportSummary(request):
    context = {
        'title': 'Summary Report',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/report/reportSummary.html", context)

def preference(request):
    context = {
        'title': 'Preferences',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/preference/preference.html", context)

def preferenceSetting(request):
    context = {
        'title': 'Setting',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/preference/preferenceSetting.html", context)
