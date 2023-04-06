from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('setting/', views.setting, name='setting'),
    path('image/upload/', views.imageUpload, name='imageUpload'),
    path('image/uploder/<str:uploader>/', views.imageUploader, name='imageUploader'),
    path('image/summary/', views.imageSummary, name='imageSummary'),
    path('image/manage/', views.imageManage, name='imageManage'),
    path('image/<int:id>/', views.imageSingle, name='imageSingle'),
    path('image/', views.image, name='image'),
    path('help/', views.help, name='help'),
    path('docs/', views.docs, name='docs'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('blog/', views.blog, name='blog'),
    path('account/profile/', views.accountProfile, name='accountProfile'),
    path('account/', views.account, name='account'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
]