from datetime import datetime
import hashlib
import os
import cv2 as cv
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
import numpy as np
from .models import XImage
from .models import XSegmentationResult
from django.utils.text import slugify
from . import forms

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
    reportSegmentation = XSegmentationResult.objects.select_related('idImage').all()
    context = {
        'title': 'Image',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'reportSegmentation': reportSegmentation,
    }
    return render(request, "myapp/image/image.html", context)



def imageUpload(request):
    ImageUploadForm = forms.ImageUploadForm()

    context = {
        'title': 'Image Upload',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'ImageUploadForm': ImageUploadForm,
    }
    if request.method == 'POST':
        files = request.FILES.getlist('image')
        for f in files:
            # hash for unique file name and time + extension
            name = hashlib.md5(f.name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + os.path.splitext(f.name)[1]
            XImage.objects.create(
                pathImage = name,
                uploader = request.POST.get('uploader'),
                slug = name,
                date = datetime.now(),
            )
            # save file to myapp/static/myapp/images folder
            with open('myapp/static/myapp/images/' + name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            # Apply kmeans to resize image
            # Convert image to a 2D array of pixels
            img = cv.imread('myapp/static/myapp/images/' + name)
            img_2d = img.astype(np.float32)
            img_2d = np.reshape(img_2d, (img.shape[0] * img.shape[1], 3))
            # Apply kmeans
            k = 2
            criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            ret, label, center = cv.kmeans(img_2d, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
            segmented = center[label.flatten()]
            segmented = segmented.reshape(img.shape)
            # Save segmented image
            name_segmented = hashlib.md5(f.name.encode('utf-8')).hexdigest() + datetime.now().strftime("%Y%m%d%H%M%S") + '_segmented' + os.path.splitext(f.name)[1]
            cv.imwrite('myapp/static/myapp/images/' + name_segmented, segmented)
            XSegmentationResult.objects.create(
                pathSegmentationKMeans = name_segmented,
                pathSegmentationAdaptive = name_segmented,
                pathGroundTruth = name_segmented,
                # report = json
                report = {
                    'kmeans': {
                        'accuracy': 0.5,
                        'precision': 0.5,
                        'recall': 0.5,
                        'f1': 0.5,
                    },
                    'adaptive': {
                        'accuracy': 0.5,
                        'precision': 0.5,
                        'recall': 0.5,
                        'f1': 0.5,
                    },
                },
                date = datetime.now(),
                idImage_id = XImage.objects.get(pathImage=name).id,
            )

        return HttpResponseRedirect('/image/manage/')

    return render(request, "myapp/image/imageUpload.html", context)

def imageSingle(request, id):
    image = XImage.objects.get(id=id)
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
    reportSegmentation = XSegmentationResult.objects.select_related('idImage').all()
    context = {
        'title': 'Image List',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'reportSegmentation': reportSegmentation,
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
