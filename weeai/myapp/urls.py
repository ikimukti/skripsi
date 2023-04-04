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
]