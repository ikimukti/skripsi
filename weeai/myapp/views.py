from django.shortcuts import render
from .models import XImage

menus = [
    {'name': 'Home', 'url': '/'},
    {'name': 'Dashboard', 'url': '/dashboard/'},
    {'name': 'Docs', 'url': '/docs/'},
    {'name': 'Blog', 'url': '/blog/'},
    {'name': 'Setting', 'url': '/setting/'},
    {'name': 'Help', 'url': '/help/'},
    {'name': 'About', 'url': '/about/'},
    {'name': 'Sign In', 'url': '/signin/'},
    {'name': 'Sign Up', 'url': '/signup/'},
    {'name': 'Sign Out', 'url': '/signout/'},
    {'name': 'Profile', 'url': '/profile/'},
    {'name': 'Image', 'url': '/image/', 'submenus': [
        {'name': 'Upload', 'url': '/image/upload/'},
        {'name': 'Manage', 'url': '/image/manage/'},
        {'name': 'Report', 'url': '/image/report/'},
    ]},
    # submenus manage
    {'name': 'Manage', 'url': '/manage/', 'submenus': [
        {'name': 'User', 'url': '/manage/user/'},
        {'name': 'Role', 'url': '/manage/role/'},
        {'name': 'Permission', 'url': '/manage/permission/'},
    ]},
    {'name': 'Report', 'url': '/report/', 'submenus': [
        {'name': 'Export Image', 'url': '/report/image/'},
        {'name': 'Export Report', 'url': '/report/report/'},
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

def singleImage(request, id):
    image = XImage.objects.get(id=id)
    context = {
        'title': 'WeeAI - Image',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
        'image': image,	
    }
    return render(request, "myapp/image/singleImage.html", context)

def uploaderImage(request, uploader):
    images = XImage.objects.filter(uploader=uploader)
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
    return render(request, "myapp/image/uploaderImage.html", context)


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

def profile(request):
    context = {
        'title': 'WeeAI - Profile',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    return render(request, "myapp/profile.html", context)
