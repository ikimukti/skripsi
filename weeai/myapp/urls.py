from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('docs/', views.docs, name='docs'),
    path('blog/', views.blog, name='blog'),
    path('setting/', views.setting, name='setting'),
    path('help/', views.help, name='help'),
    path('image/', views.image, name='image'),
    path('image/<int:id>/', views.image, name='image/id'),
    path('about/', views.about, name='about'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]