from datetime import datetime
from django.shortcuts import render
from .models import XImage
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
        {'name': 'Export Image', 'url': '/report/image/'},
        {'name': 'Export Report', 'url': '/report/report/'},
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
    return render(request, "myapp/setting.html", context)

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
    images = XImage.objects.all()
    context = {
        'title': 'WeeAI - Image',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'images': images,	
    }
    return render(request, "myapp/image.html", context)



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
        form = forms.ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            myimage = form.cleaned_data['file']
            print(myimage)
        print(request.FILES)
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
    return render(request, "myapp/signin.html", context)

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
    return render(request, "myapp/signup.html", context)

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
    return render(request, "myapp/signout.html", context)

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
    return render(request, "myapp/account.html", context)

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
