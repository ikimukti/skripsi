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
    {'name': 'Home', 'url': '/'},
    {'name': 'Dashboard', 'url': '/dashboard/'},
    {'name': 'Sign In', 'url': '/signin/'},
    {'name': 'Sign Up', 'url': '/signup/'},
    {'name': 'Sign Out', 'url': '/signout/'},
    {'name': 'Account', 'url': '/account/', 'submenus': [
        {'name': 'Profile', 'url': '/account/profile/'},
    ]},
    {'name': 'Image', 'url': '/image/', 'submenus': [
        {'name': 'Upload', 'url': '/image/upload/'},
        {'name': 'Manage', 'url': '/image/manage/'},
        {'name': 'Summary', 'url': '/image/summary/'},
    ]},
    # submenus manage
    {'name': 'Manage', 'url': '/manage/', 'submenus': [
        {'name': 'User', 'url': '/manage/user/'},
        {'name': 'Role', 'url': '/manage/role/'},
        {'name': 'Permission', 'url': '/manage/permission/'},
    ]},
    {'name': 'Report', 'url': '/report/', 'submenus': [
        {'name': 'Segmentation', 'url': '/report/segmentation/'},
        {'name': 'Export Image', 'url': '/report/export/image/'},
        {'name': 'Export Report', 'url': '/report/export/report/'},
        {'name': 'Summary', 'url': '/report/summary/'},
    ]},
    {'name': 'Preference', 'url': '/preference/', 'submenus': [
        {'name': 'Setting', 'url': '/preference/setting/'},
        {'name': 'Help', 'url': '/help/'},
        {'name': 'Docs', 'url': '/docs/'},
        {'name': 'Blog', 'url': '/blog/'},
        {'name': 'About', 'url': '/about/'},
    ]},
]


# Create your views here.
def index(request):
    context = {
        'title': 'WeeAI - Home',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'contributor': 'WeeAI Team',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/index.html", context)

def dashboard(request):
    context = {
        'title': 'WeeAI - Dashboard',
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
        'title': 'WeeAI - Docs',
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
        'title': 'WeeAI - Blog',
        'contributor': 'WeeAI Team',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/blog.html", context)

def setting(request):
    context = {
        'title': 'WeeAI - Setting',
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
        'title': 'WeeAI - Help',
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
        'title': 'WeeAI - Image',
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
        'title': 'WeeAI - Image Upload',
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
        'title': 'WeeAI - Image Single',
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
        'title': 'WeeAI - Image Uploader',
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
        'title': 'WeeAI - Image Summary',
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
        'title': 'WeeAI - Image Manage',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'images': images,	
    }
    return render(request, "myapp/image/imageManage.html", context)

def about(request):
    context = {
        'title': 'WeeAI - About',
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
        'title': 'WeeAI - Sign In',
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
        'title': 'WeeAI - Sign Up',
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
        'title': 'WeeAI - Sign Out',
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
        'title': 'WeeAI - Account',
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
        'title': 'WeeAI - Profile',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/account/profile.html", context)

def manage(request):
    context = {
        'title': 'WeeAI - Manage',
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
        'title': 'WeeAI - Manage User',
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
        'title': 'WeeAI - Manage Role',
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
        'title': 'WeeAI - Manage Permission',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/manage/managePermission.html", context)

def report(request):
    context = {
        'title': 'WeeAI - Report',
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
        'title': 'WeeAI - Segmentation Report',
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
        'title': 'WeeAI - Export Image Report',
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
        'title': 'WeeAI - Export Report',
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
        'title': 'WeeAI - Summary Report',
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
        'title': 'WeeAI - Preference',
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
        'title': 'WeeAI - Setting',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/preference/preferenceSetting.html", context)
