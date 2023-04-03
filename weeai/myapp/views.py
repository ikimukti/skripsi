from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'WeeAI - Home',
        'content': 'Welcome to WeeAI!',
        'menus' : [
            {'name': 'Home', 'url': ''},
            {'name': 'Dashboard', 'url': 'dashboard'},
            {'name': 'Docs', 'url': 'docs'},
            {'name': 'Blog', 'url': 'blog'},
            {'name': 'Setting', 'url': 'setting'},
            {'name': 'Help', 'url': 'help'},
            {'name': 'About', 'url': 'about'},
            {'name': 'Sign In', 'url': 'signin'},
            {'name': 'Sign Up', 'url': 'signup'},
            {'name': 'Sign Out', 'url': 'signout'},
            {'name': 'Profile', 'url': 'profile'},
            # submenus manage admin
            {'name': 'Admin', 'url': 'admin', 'submenus': [
                {'name': 'Admin', 'url': 'admin'},
                {'name': 'Admin', 'url': 'admin'},
                {'name': 'Admin', 'url': 'admin'},
            ]},
        
        ]
    }
    return render(request, "myapp/index.html", context)

def dashboard(request):
    return render(request, "myapp/dashboard.html")

def docs(request):
    return render(request, "myapp/docs.html")

def blog(request):
    return render(request, "myapp/blog.html")

def setting(request):
    return render(request, "myapp/setting.html")

def help(request):
    return render(request, "myapp/help.html")