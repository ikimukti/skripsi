from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('setting/', views.setting, name='setting'),
    path('profile/', views.profile, name='profile'),
    path('image/u/<str:uploader>/', views.uploaderImage, name='uploaderImage'),
    path('image/<int:id>/', views.singleImage, name='singleImage'),
    path('image/', views.image, name='image'),
    path('help/', views.help, name='help'),
    path('docs/', views.docs, name='docs'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
]