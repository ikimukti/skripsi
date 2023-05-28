from datetime import datetime
import hashlib
import os
import cv2 as cv
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
import numpy as np
from .models import XImage, XSegmentationResult
from django.utils.text import slugify
from .forms import ImageUploadForm
from django.db.models import OuterRef, Subquery, Q
from django.core.paginator import Paginator
import sweetify
from django.contrib import messages
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, rand_score, jaccard_score, mean_squared_error, mean_absolute_error
from matplotlib import pyplot as plt
from .utils import get_plot, get_graph, get_plot_table

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

class IndexClassView(View):
    context = {
        'title': 'Home',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'contributor': 'WeeAI Team',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/index.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

def calculate_scores(ground_truth, segmented, type, average='binary', zero_division=1, scaleRatio=None, contrastEnhancement=None, GroundTruthKe=None):
    scores = {}
    scores['type'] = type
    if type == 'kmeans':
        average = 'weighted'
    scores['f1'] = str(round(f1_score(ground_truth.flatten(), segmented.flatten(), average=average, zero_division=zero_division), 4))
    if scores['f1'] == 'nan' or scores['f1'] == 'inf' or scores['f1'] == '-inf' or scores['f1'] == 'None' or scores['f1'] == '0.0' or scores['f1'] == '0':
        # reverse segmented value
        reverse_segmented = np.where(segmented == 0, 1, 0)
        scores['f1'] = str(round(f1_score(ground_truth.flatten(), reverse_segmented.flatten(), average=average, zero_division=zero_division), 4))
        
    scores['precision'] = str(round(precision_score(ground_truth.flatten(), segmented.flatten(), average=average, zero_division=zero_division), 4))
    if scores['precision'] == 'nan' or scores['precision'] == 'inf' or scores['precision'] == '-inf' or scores['precision'] == 'None' or scores['precision'] == '0.0' or scores['precision'] == '0':
        # reverse segmented value
        reverse_segmented = np.where(segmented == 0, 1, 0)
        scores['precision'] = str(round(precision_score(ground_truth.flatten(), reverse_segmented.flatten(), average=average, zero_division=zero_division), 4))
    scores['recall'] = str(round(recall_score(ground_truth.flatten(), segmented.flatten(), average=average, zero_division=zero_division), 4))
    if scores['recall'] == 'nan' or scores['recall'] == 'inf' or scores['recall'] == '-inf' or scores['recall'] == 'None' or scores['recall'] == '0.0' or scores['recall'] == '0':
        # reverse segmented value
        reverse_segmented = np.where(segmented == 0, 1, 0)
        scores['recall'] = str(round(recall_score(ground_truth.flatten(), reverse_segmented.flatten(), average=average, zero_division=zero_division), 4))
    
    scores['accuracy'] = str(round(accuracy_score(ground_truth.flatten(), segmented.flatten()), 4))
    if scores['accuracy'] == 'nan' or scores['accuracy'] == 'inf' or scores['accuracy'] == '-inf' or scores['accuracy'] == 'None' or scores['accuracy'] == '0.0' or scores['accuracy'] == '0':
        # reverse segmented value
        reverse_segmented = np.where(segmented == 0, 1, 0)
        scores['accuracy'] = str(round(accuracy_score(ground_truth.flatten(), reverse_segmented.flatten()), 4))
    scores['rand'] = str(round(rand_score(ground_truth.flatten(), segmented.flatten()), 4))
    if scores['rand'] == 'nan' or scores['rand'] == 'inf' or scores['rand'] == '-inf' or scores['rand'] == 'None' or scores['rand'] == '0.0' or scores['rand'] == '0':
        # reverse segmented value
        reverse_segmented = np.where(segmented == 0, 1, 0)
        scores['rand'] = str(round(rand_score(ground_truth.flatten(), reverse_segmented.flatten()), 4))
    scores['jaccard'] = str(round(jaccard_score(ground_truth.flatten(), segmented.flatten(), average=average, zero_division=zero_division), 4))
    if scores['jaccard'] == 'nan' or scores['jaccard'] == 'inf' or scores['jaccard'] == '-inf' or scores['jaccard'] == 'None' or scores['jaccard'] == '0.0' or scores['jaccard'] == '0':
        # reverse segmented value
        reverse_segmented = np.where(segmented == 0, 1, 0)
        scores['jaccard'] = str(round(jaccard_score(ground_truth.flatten(), reverse_segmented.flatten(), average=average, zero_division=zero_division), 4))
    mse = np.mean((ground_truth - segmented) ** 2)
    scores['mse'] = str(round(mse, 4))
    scores['mae'] = str(round(mean_absolute_error(ground_truth.flatten(), segmented.flatten()), 4))
    scores['rmse'] = str(round(mean_squared_error(ground_truth.flatten(), segmented.flatten(), squared=False), 4))
    if mse == 0:
        scores['psnr'] = 'inf'
    else:
        scores['psnr'] = str(round(10 * np.log10((255 ** 2) / np.mean((ground_truth - segmented) ** 4)), 4))
    if scaleRatio is not None:
        scores['scaleRatio'] = scaleRatio
    if contrastEnhancement is not None:
        scores['contrastEnhancement'] = contrastEnhancement
    if GroundTruthKe is not None:
        scores['GroundTruthKe'] = GroundTruthKe
    
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

class ContactClassView(View):
    context = {
        'title': 'Contact',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/contact.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class DashboardClassView(View):
    context = {
        'title': 'Dashboard',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/dashboard.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class DocsClassView(View):
    context = {
        'title': 'Docs',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/docs.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class BlogClassView(View):
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
    template_name = 'myapp/blog.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class SettingClassView(View):
    context = {
        'title': 'Settings',
        'contributor': 'WeeAI Team',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/preference/preferenceSetting.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class HelpClassView(View):
    context = {
        'title': 'Help',
        'contributor': 'WeeAI Team',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/help.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)
    
class AboutClassView(View):
    context = {
        'title': 'About',
        'contributor': 'WeeAI Team',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/about.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)
    
class SignInClassView(View):
    context = {
        'title': 'Sign In',
        'contributor': 'WeeAI Team',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/system/signin.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)
    
class SignUpClassView(View):
    context = {
        'title': 'Sign Up',
        'contributor': 'WeeAI Team',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/system/signup.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class SignOutClassView(View):
    context = {
        'title': 'Sign Out',
        'contributor': 'WeeAI Team',
        'content': 'Welcome to WeeAI!',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/system/signout.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class AccountClassView(View):
    context = {
        'title': 'Account',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/account/account.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class AccountProfileClassView(View):
    context = {
        'title': 'Profile',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/account/accountProfile.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class AccountChangePasswordClassView(View):
    context = {
        'title': 'Change Password',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/manage/password.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)
    
class ManageClassView(View):
    context = {
        'title': 'Manage Account',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/manage/manage.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)
    
class ManageUserClassView(View):
    context = {
        'title': 'Manage User',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/manage/manageUser.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)
    
class ManageRoleClassView(View):
    context = {
        'title': 'Manage Role',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/manage/manageRole.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class ManagePermissionClassView(View):
    context = {
        'title': 'Manage Permission',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/manage/managePermission.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class ManageGroupClassView(View):
    context = {
        'title': 'Manage Group',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/manage/manageGroup.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class ReportClassView(View):
    context = {
        'title': 'Report',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/report.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/report/report.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)
    
class ReportSegmentationClassView(View):
    context = {
        'title': 'Segmentation Report',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/report.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/report/reportSegmentation.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class ReportExportImageClassView(View):
    context = {
        'title': 'Export Image Report',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/report.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/report/reportExportImage.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class ReportExportReportClassView(View):
    context = {
        'title': 'Export Report',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/report.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/report/reportExportReport.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class ReportSummaryClassView(View):
    context = {
        'title': 'Summary Report',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/report.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/report/reportSummary.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class PreferenceClassView(View):
    context = {
        'title': 'Preferences',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/preference.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/preference/preference.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class PreferenceSettingClassView(View):
    context = {
        'title': 'Setting',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/preference.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/preference/preferenceSetting.html'
    # override method get
    def get(self, request):
        return render(request, self.template_name, self.context)

class ImageClassView(View):
    context = {
        'title': 'Image',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/image.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/image/image.html'
    # override method get
    def get(self, request):
        # Mendapatkan XSegmentationResult terkait jika ada (hanya 1) dan buat field baru xsegmentation_result
        xsegmentation_results = XSegmentationResult.objects.filter(idImage=OuterRef('pk'))
        # Definisikan semua field yang ingin diambil
        fields = [
            'report',
            'id',
            'idImage',
            'pathPreprocessing',
            'pathSegmentationResult',
            'dateCreated',
            'dateModified',
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
            ).order_by('-dateModified')
        else:
            # Mendapatkan semua objek XImage
            ximages = XImage.objects.all().order_by('-dateModified')
        # Anotasi XImage dengan field-field yang diambil
        images = ximages.annotate(**xsegmentation_result_fields)
        # pagination
        paginator = Paginator(images, 10)
        page_list = request.GET.get('page')
        images = paginator.get_page(page_list)
        self.context['images'] = images
        return render(request, self.template_name, self.context)

class ImageListClassView(View):
    context = {
        'title': 'Image List',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/image.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/image/image.html'
    # override method get
    def get(self, request):
        # Mendapatkan XSegmentationResult terkait jika ada (hanya 1) dan buat field baru xsegmentation_result
        xsegmentation_results = XSegmentationResult.objects.filter(idImage=OuterRef('pk'))
        # Definisikan semua field yang ingin diambil
        fields = [
            'report',
            'id',
            'idImage',
            'pathPreprocessing',
            'pathSegmentationResult',
            'dateCreated',
            'dateModified',
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
            ).order_by('-dateModified')
        else:
            # Mendapatkan semua objek XImage
            ximages = XImage.objects.all().order_by('-dateModified')
        # Anotasi XImage dengan field-field yang diambil
        images = ximages.annotate(**xsegmentation_result_fields)
        # pagination
        paginator = Paginator(images, 10)
        page_list = request.GET.get('page')
        images = paginator.get_page(page_list)
        self.context['images'] = images
        return render(request, self.template_name, self.context)

class ImageManageClassView(View):
    context = {
        'title': 'Image Manage',	
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/image.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/image/imageManage.html'
    # override method get
    def get(self, request):
        # Mendapatkan XSegmentationResult terkait jika ada (hanya 1) dan buat field baru xsegmentation_result
        xsegmentation_results = XSegmentationResult.objects.filter(idImage=OuterRef('pk'))
        # Definisikan semua field yang ingin diambil
        fields = [
            'report',
            'id',
            'idImage',
            'pathPreprocessing',
            'pathSegmentationResult',
            'dateCreated',
            'dateModified',
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
            ).order_by('-dateModified')
        else:
            # Mendapatkan semua objek XImage
            ximages = XImage.objects.all().order_by('-dateModified')
        # Anotasi XImage dengan field-field yang diambil
        images = ximages.annotate(**xsegmentation_result_fields)
        # pagination
        paginator = Paginator(images, 10)
        page_list = request.GET.get('page')
        images = paginator.get_page(page_list)
        self.context['images'] = images
        return render(request, self.template_name, self.context)

class ImageSummaryClassView(View):
    context = {
        'title': 'Image Summary',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/image.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/image/imageSummary.html'
    # override method get
    def get(self, request):
        # meembuat data untuk chart
        x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
        y = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
        # get_plot(x, y, title, xlabel, ylabel, rotation, figsize, tight_layout)
        chart = get_plot(x, y, 'Contoh Chart', 'X', 'Y', 0, (10, 5), True)
        self.context['chart'] = chart
        # Mendapatkan XSegmentationResult terkait jika ada (hanya 1) dan buat field baru xsegmentation_result
        xsegmentation_results = XSegmentationResult.objects.filter(idImage=OuterRef('pk'))
        # Definisikan semua field yang ingin diambil
        fields = [
            'report',
            'id',
            'idImage',
            'pathPreprocessing',
            'pathSegmentationResult',
            'dateCreated',
            'dateModified',
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
            ).order_by('-dateModified').distinct()
        else:
            # Mendapatkan semua objek XImage
            ximages = XImage.objects.all().order_by('-dateModified').distinct()
        # Anotasi XImage dengan field-field yang diambil
        images = ximages.annotate(**xsegmentation_result_fields)
        # pagination
        paginator = Paginator(images, 10)
        page_list = request.GET.get('page')
        images = paginator.get_page(page_list)
        self.context['images'] = images
        return render(request, self.template_name, self.context)
    
class ImageSummarySingleClassView(View):
    context = {
        'title': 'Image Summary',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/image.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/image/imageSummary.html'
    def generate_chart(self, title, chartName, y_labels,unit):
        data = self.context['imageSingle']['xsegmentation_result_report']['kmeans_scores']

        # x adalah kombinasi dari 'scaleRatio', 'contrastEnhancement' 'GroundTruthKe'
        x = [f"{item['scaleRatio']},{item['contrastEnhancement']},{item['GroundTruthKe']}" for item in data]

        xlabel = 'Kombinasi Parameter (scaleRatio, contrastEnhancement, GroundTruthKe)'

        # x adalah kombinasi dari scaleRatio / 10, contrastEnhancement / 10,  GroundTruthKe
        x = [f"{item['scaleRatio']/10}:1 , {item['contrastEnhancement']/10}:1 , {item['GroundTruthKe']}" for item in data]

        y_labels = y_labels
        if unit == '%':
            # y_values * 100
            y_values = [[float(item[label]) * 100 for item in data] for label in y_labels]
        else:
            y_values = [[float(item[label]) for item in data] for label in y_labels]
        title = title
        rotation = 0
        figsize = (10, 5)
        tight_layout = True

        # Mark the best x in red
        # Find the index of the best y value
        best_index = x.index(max(x))

        # Create a list of colors
        colors = ['blue'] * len(x)
        colors[best_index] = 'red'

        chart = get_plot(x, y_values, title, xlabel, y_labels, rotation, figsize, tight_layout, colors, unit)
        
        self.context[chartName] = chart

    # override method get
    def get(self, request, id):
        
        ximage = XImage.objects.prefetch_related('xsegmentationresult_set').get(id=id)

        if ximage.xsegmentationresult_set.exists():
            xsegmentation_result = ximage.xsegmentationresult_set.first()
            # Mengambil semua field yang dibutuhkan dari XSegmentationResult
            xsegmentation_result_fields = {
                'xsegmentation_result_report': xsegmentation_result.report,
                'xsegmentation_result_id': xsegmentation_result.id,
                'xsegmentation_result_idImage': xsegmentation_result.idImage,
                'xsegmentation_result_pathPreprocessing': xsegmentation_result.pathPreprocessing,
                'xsegmentation_result_pathSegmentationResult': xsegmentation_result.pathSegmentationResult,
                'xsegmentation_result_dateCreated': xsegmentation_result.dateCreated,
                'xsegmentation_result_dateModified': xsegmentation_result.dateModified,
            }
        
            self.context['imageSingle'] = {
                **ximage.__dict__,
                **xsegmentation_result_fields,
            }
        else:
            self.context['imageSingle'] = ximage.__dict__
        
        y_labels = ['mse', 'mae', 'rmse', 'psnr']
        self.generate_chart('Akurasi K-Means', 'chartKmeans', y_labels,unit='dB')
        self.generate_chart('Akurasi Adaptive Thresholding', 'chartAdaptive', y_labels,unit='dB')
        y_labels = ['f1', 'precision', 'recall', 'accuracy','rand', 'jaccard']
        self.generate_chart('Akurasi K-Means', 'chartKmeans2', y_labels, unit='%')
        self.generate_chart('Akurasi Adaptive Thresholding', 'chartAdaptive2', y_labels, unit='%')
        
        
        
        return render(request, self.template_name, self.context)

class ImageUploaderClassView(View):
    context = {
        'title': 'Image Uploader',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/styles.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/image/imageUploader.html'
    # override method get
    def get(self, request, uploader):
        # Mendapatkan XSegmentationResult terkait jika ada (hanya 1) dan buat field baru xsegmentation_result
        xsegmentation_results = XSegmentationResult.objects.filter(idImage=OuterRef('pk'))
        # Definisikan semua field yang ingin diambil
        fields = [
            'report',
            'id',
            'idImage',
            'pathPreprocessing',
            'pathSegmentationResult',
            'dateCreated',
            'dateModified',
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
            ).order_by('-dateModified').distinct()
        else:
            # Mendapatkan semua objek XImage
            ximages = XImage.objects.filter(uploader=uploader).order_by('-dateModified').distinct()
        print('Uploader: ', uploader)
        # Anotasi XImage dengan field-field yang diambil
        images = ximages.annotate(**xsegmentation_result_fields)
        paginator = Paginator(images, 10)
        page_list = request.GET.get('page')
        images = paginator.get_page(page_list)
        self.context['images'] = images
        self.context['imageUploader'] = uploader
        return render(request, self.template_name, self.context)

class ImageSingleClassView(View):
    context = {
        'title': 'Image Single',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/style.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/image/imageSingle.html'
    # override method get
    def get(self, request, id):
        ximage = XImage.objects.prefetch_related('xsegmentationresult_set').get(id=id)

        if ximage.xsegmentationresult_set.exists():
            xsegmentation_result = ximage.xsegmentationresult_set.first()
            # Mengambil semua field yang dibutuhkan dari XSegmentationResult
            xsegmentation_result_fields = {
                'xsegmentation_result_report': xsegmentation_result.report,
                'xsegmentation_result_id': xsegmentation_result.id,
                'xsegmentation_result_idImage': xsegmentation_result.idImage,
                'xsegmentation_result_pathPreprocessing': xsegmentation_result.pathPreprocessing,
                'xsegmentation_result_pathSegmentationResult': xsegmentation_result.pathSegmentationResult,
                'xsegmentation_result_dateCreated': xsegmentation_result.dateCreated,
                'xsegmentation_result_dateModified': xsegmentation_result.dateModified,
            }
        
            self.context['image'] = {
                **ximage.__dict__,
                **xsegmentation_result_fields,
            }
        else:
            self.context['image'] = ximage.__dict__
            
        return render(request, self.template_name, self.context)

def plot_and_save(scores):
    # Extract F1 scores
    f1_scores = [float(scores[key]['f1']) for key in scores]

    # Extract corresponding configurations for x-axis labels
    x_labels = [str(key) for key in scores]

    # Plot the F1 scores
    plt.bar(range(len(f1_scores)), f1_scores)
    plt.xlabel('Configurations')
    plt.ylabel('F1 Score')
    plt.title('F1 Scores for Different Configurations')
    plt.xticks(range(len(f1_scores)), x_labels, rotation=90)
    plt.tight_layout()
    # Saving the plot as an image
    plt.savefig('result_scores.png')
    

def kmeans_segmentation_scores(image_path, k=2, scaleRatio=1.0, contrastEnhancement=1.0, imgGroundTruth=None, imgGroundTruth2=None):
    img = image_path

    scores = []
    scaleRatio = float(scaleRatio)
    contrastEnhancement = float(contrastEnhancement)
    contrastEnhancement2 = float(contrastEnhancement)
    
    #  Create for loops with a scaleRatio range from 0.3 before scaleRatio and 0.3 from after scaleRatio
    if scaleRatio <= 0.1:
        beforeScaleRatio = 0.1 * 10
    else:
        beforeScaleRatio = (scaleRatio - 0.3) * 10
    afterScaleRatio = (scaleRatio + 0.3) * 10
    for i in range(int(beforeScaleRatio), int(afterScaleRatio), 1):
        # Resize the image
        imgScale = cv.resize(img, (int(img.shape[1] * i / 10), int(img.shape[0] * i / 10)))
        print('imgScale: ', imgScale.shape)
        imgGT = cv.resize(imgGroundTruth, (int(imgGroundTruth.shape[1] * i / 10), int(imgGroundTruth.shape[0] * i / 10)))
        print('imgGT: ', imgGT.shape)
        imgGT2 = cv.resize(imgGroundTruth2, (int(imgGroundTruth2.shape[1] * i / 10), int(imgGroundTruth2.shape[0] * i / 10)))
        # Convert imgGT2 to 3 channels
        imgGT2 = cv.cvtColor(imgGT2, cv.COLOR_GRAY2BGR)
        print('imgGT2: ', imgGT2.shape)
        # Convert image to BGR if necessary
        if len(imgScale.shape) == 3 and imgScale.shape[2] == 4:
            imgScale = cv.cvtColor(imgScale, cv.COLOR_BGRA2BGR)
        elif len(imgScale.shape) == 2:
            imgScale = cv.cvtColor(imgScale, cv.COLOR_GRAY2BGR)
        # create for loop with range contrastEnhancement from 1 before contrastEnhancement and 2 from after contrastEnhancement
        if contrastEnhancement <= 0.1:
            beforeContrastEnhancement = 0.1 * 10
        else:
            beforeContrastEnhancement = (contrastEnhancement - 0.3) * 10
        afterContrastEnhancement = (contrastEnhancement + 0.3) * 10
        print('Scale Ratio: ', i/10)
        for j in range(int(beforeContrastEnhancement), int(afterContrastEnhancement), 1):
            print('Contrast Enhancement: ', j/10)
            # Image contrastEnhancement with method 1
            contrastEnhancementimg = cv.addWeighted(imgScale, j/10, np.zeros(imgScale.shape, imgScale.dtype), 0, 0)
            gray_img = cv.cvtColor(imgScale, cv.COLOR_BGR2GRAY)
            # Image contrastEnhancement with method 2
            gray_img = cv.convertScaleAbs(gray_img, alpha=j/10, beta=0)
            contrastEnhancement2img = cv.equalizeHist(gray_img, j/10)
            
            # Convert image to RGB
            img_rgb = cv.cvtColor(contrastEnhancementimg, cv.COLOR_BGR2RGB)
            img_rgb2 = cv.cvtColor(contrastEnhancement2img, cv.COLOR_BGR2RGB)

            # Convert to float type
            img_2d = img_rgb.astype(np.float32)
            img_2d2 = img_rgb2.astype(np.float32)

            # Reshape image to 2D array
            img_2d = img_2d.reshape(img_2d.shape[0] * img_2d.shape[1], img_2d.shape[2])
            img_2d2 = img_2d2.reshape(img_2d2.shape[0] * img_2d2.shape[1], img_2d2.shape[2])

            # Apply k-means clustering
            criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            criteria2 = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            ret, labels, centers = cv.kmeans(img_2d, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
            ret2, labels2, centers2 = cv.kmeans(img_2d2, k, None, criteria2, 10, cv.KMEANS_RANDOM_CENTERS)

            # Convert center values to uint8
            centers = np.uint8(centers)
            centers2 = np.uint8(centers2)

            # Map labels to center values
            segmented_img = centers[labels.flatten()]
            segmented_img2 = centers2[labels2.flatten()]
            segmented_img = segmented_img.reshape(img_rgb.shape)
            segmented_img2 = segmented_img2.reshape(img_rgb2.shape)
            scores.append(calculate_scores(imgGT, segmented_img, type='kmeans', scaleRatio=i, contrastEnhancement=j, GroundTruthKe=1))
            scores.append(calculate_scores(imgGT2, segmented_img2, type='kmeans', scaleRatio=i, contrastEnhancement=j, GroundTruthKe=2))


            
    return scores
            
    
def kmeans_segmentation(image_path, k=2):
    # Read the image
    img = image_path
    
    # Convert image to RGB
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Convert to float type
    img_2d = img_rgb.astype(np.float32)

    # Reshape image to 2D array
    img_2d = img_2d.reshape(img_2d.shape[0] * img_2d.shape[1], img_2d.shape[2])

    # Apply k-means clustering
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, labels, centers = cv.kmeans(img_2d, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

    # Convert center values to uint8
    centers = np.uint8(centers)

    # Map labels to center values
    segmented_img = centers[labels.flatten()]
    segmented_img = segmented_img.reshape(img_rgb.shape)

    return segmented_img

def adaptive_threshold_segmentation(image_path, block_size, c):
    # Read the image
    img = image_path
    # Check if image is grayscale
    if len(img.shape) > 2:
        # Convert image to grayscale
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    else:
        img = img
    # Apply adaptive thresholding
    segmented_img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, block_size, c)

    return segmented_img

def otsu_threshold_segmentation(image_path):
    # Read the image
    img = image_path
    # Check if image is grayscale
    if len(img.shape) > 2:
        # Convert image to grayscale
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    else:
        img = img
    # Apply Otsu's thresholding
    _, segmented_img = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    return segmented_img

def canny_segmentation(image_path, threshold1, threshold2):
    # Read the image
    img = image_path

    # Apply Canny edge detection
    edges = cv.Canny(img, threshold1, threshold2)
    segmented_img = cv.bitwise_and(img, img, mask=edges)

    return segmented_img

def sobel_segmentation(image_path):
    # Read the image
    img = image_path

    # Apply Sobel edge detection
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
    segmented_img = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

    return segmented_img

def prewitt_segmentation(image_path):
    # Read the image
    img = image_path

    # Apply Prewitt edge detection
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    img_prewittx = cv.filter2D(img, -1, kernelx)
    img_prewitty = cv.filter2D(img, -1, kernely)
    segmented_img = cv.bitwise_or(img_prewittx, img_prewitty)

    return segmented_img

def ground_truth_image(image_path):
    
    # Read the image
    img = image_path

    # Create a blank ground truth image
    ground_truth = np.zeros_like(img)
    ground_truth = np.reshape(ground_truth, img.shape)

    # Set black areas as foreground (255) and white areas as background (0)
    ground_truth[img < 127] = 255

    # If the black area is the background, invert the image
    if np.sum(ground_truth[0]) > np.sum(ground_truth[-1]):
        ground_truth = cv.bitwise_not(ground_truth)
    return ground_truth

def find_histogram(labels, centers):
    hist = cv.calcHist([labels.astype(np.float32)], [0], None, [3], [0, 3])
    hist = hist.flatten()
    return hist



def plot_colors2(hist, centers):
    # Implementation for plotting colors
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    for (percent, color) in zip(hist, centers):
        # Plotting colors
        endX = startX + (percent * 300)
        cv.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
        startX = endX
    return bar

            
def adaptive_threshold_segmentation_scores(image_path, block_size, c, scaleRatio=1.0, contrastEnhancement=1.0, imgGroundTruth=None, imgGroundTruth2=None):
    img = image_path

    scores = []
    scaleRatio = float(scaleRatio)
    contrastEnhancement = float(contrastEnhancement)
    contrastEnhancement2 = float(contrastEnhancement)
    
    #  Create for loops with a scaleRatio range from 0.3 before scaleRatio and 0.3 from after scaleRatio
    if scaleRatio <= 0.1:
        beforeScaleRatio = 0.1 * 10
    else:
        beforeScaleRatio = (scaleRatio - 0.3) * 10
    afterScaleRatio = (scaleRatio + 0.3) * 10
    for i in range(int(beforeScaleRatio), int(afterScaleRatio), 1):
        # Resize the image
        imgScale = cv.resize(img, (int(img.shape[1] * i / 10), int(img.shape[0] * i / 10)))
        print('imgScale: ', imgScale.shape)
        imgGT = cv.resize(imgGroundTruth, (int(imgGroundTruth.shape[1] * i / 10), int(imgGroundTruth.shape[0] * i / 10)))
        print('imgGT: ', imgGT.shape)
        imgGT2 = cv.resize(imgGroundTruth2, (int(imgGroundTruth2.shape[1] * i / 10), int(imgGroundTruth2.shape[0] * i / 10)))
        # Convert imgGT2 to 3 channels
        imgGT2 = cv.cvtColor(imgGT2, cv.COLOR_GRAY2BGR)
        print('imgGT2: ', imgGT2.shape)
        # Convert image to BGR if necessary
        if len(imgScale.shape) == 3 and imgScale.shape[2] == 4:
            imgScale = cv.cvtColor(imgScale, cv.COLOR_BGRA2BGR)
        elif len(imgScale.shape) == 2:
            imgScale = cv.cvtColor(imgScale, cv.COLOR_GRAY2BGR)
        # create for loop with range contrastEnhancement from 1 before contrastEnhancement and 2 from after contrastEnhancement
        if contrastEnhancement <= 0.1:
            beforeContrastEnhancement = 0.1 * 10
        else:
            beforeContrastEnhancement = (contrastEnhancement - 0.3) * 10
        afterContrastEnhancement = (contrastEnhancement + 0.3) * 10
        print('Scale Ratio: ', i/10)
        for j in range(int(beforeContrastEnhancement), int(afterContrastEnhancement), 1):
            print('Contrast Enhancement: ', j/10)
            # Image contrastEnhancement with method 1
            contrastEnhancementimg = cv.addWeighted(imgScale, j/10, np.zeros(imgScale.shape, imgScale.dtype), 0, 0)
            gray_img = cv.cvtColor(imgScale, cv.COLOR_BGR2GRAY)
            contrastEnhancementimg = cv.cvtColor(contrastEnhancementimg, cv.COLOR_BGR2GRAY)
            # Image contrastEnhancement with method 2
            gray_img = cv.convertScaleAbs(gray_img, alpha=j/10, beta=0)
            contrastEnhancementimg2 = cv.equalizeHist(gray_img, j/10)
            
            # Apply adaptive thresholding
            segmented_img = cv.adaptiveThreshold(contrastEnhancementimg, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, block_size, c)
            segmented_img2 = cv.adaptiveThreshold(contrastEnhancementimg2, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, block_size, c)
            # 3 channels for segmented_img
            segmented_img = cv.cvtColor(segmented_img, cv.COLOR_GRAY2BGR)
            segmented_img2 = cv.cvtColor(segmented_img2, cv.COLOR_GRAY2BGR)
            
            # Calculate scores
            scores.append(calculate_scores(imgGT, segmented_img, type='adaptive', scaleRatio=i, contrastEnhancement=j, GroundTruthKe=1, average='weighted'))
            scores.append(calculate_scores(imgGT2, segmented_img2, type='adaptive', scaleRatio=i, contrastEnhancement=j, GroundTruthKe=2, average='weighted'))

            
    return scores
    

class ImageUploadClassView(View):
    context = {
        'title': 'Image Upload',
        'content': 'Welcome to WeeAI!',
        'contributor': 'WeeAI Team',
        'app_css': 'myapp/css/image.css',
        'app_js': 'myapp/js/scripts.js',
        'menus': menus,
        'logo': 'myapp/images/Logo.png',
    }
    template_name = 'myapp/image/imageUpload.html'
    # override method get
    def get(self, request):
        self.context['title'] = 'Image Upload Get'
        image_upload_form = ImageUploadForm()
        self.context['ImageUploadForm'] = image_upload_form
        return render(request, self.template_name, self.context)
    
    
    
    
    def post(self, request):
        self.context['title'] = 'Image Upload Post'
        files = request.FILES.getlist('image')
        existing_files = [f.name for f in os.scandir('myapp/static/myapp/images/') if f.is_file()]
        # request.POST.get CharField
        POSTuploader = request.POST.get('uploader')
        POSTnameImage = request.POST.get('nameImage')
        POSTbackgroundDominantColor = request.POST.get('backgroundDominantColor')
        # request.POST.get FloatField
        POSTscaleRatio = request.POST.get('scaleRatio')
        POSTcontrastEnhancement = request.POST.get('contrastEnhancement')
        POSTdistanceObject = request.POST.get('distanceObject')
        # request.POST.get BooleanField
        POSTnoiseReduction = request.POST.get('noiseReduction')
        # upload file
        for file in files:
            # hash for unique file name and time + extension
            name = hashlib.md5(str(datetime.now()).encode('utf-8')).hexdigest() + '.' + file.name.split('.')[-1]
            
            if name not in existing_files:
                # save file
                with open('myapp/static/myapp/images/' + name, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                    existing_files.append(name)
            else:
                print(f"File {name} already exists and will not be uploaded.")
            img = cv.imread('myapp/static/myapp/images/' + name)
            # Find and save the dominant color
            imgDominantColor = img.copy()
            imgDominantColor = cv.cvtColor(imgDominantColor, cv.COLOR_BGR2RGB)
            imgDominantColor = imgDominantColor.reshape((imgDominantColor.shape[0] * imgDominantColor.shape[1], 3)).astype(np.float32)

            criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 200, 0.1)
            flags = cv.KMEANS_RANDOM_CENTERS

            _, labels, centers = cv.kmeans(imgDominantColor, 3, None, criteria, 10, flags)

            hist = find_histogram(labels, centers)
            bar = plot_colors2(hist, centers)

            # plt.axis("off")
            # plt.imshow(bar)
            # plt.savefig('myapp/static/myapp/images/' + name + '_dominantColor.jpg', bbox_inches='tight', pad_inches=0)
            # pathDominantColor = name + '_dominantColor.jpg'
            # Image preprocessing
            pathPreprocessingOriginal = name
            height, width, channels = img.shape
            # Image scaleRatio
            scaleRatio = float(POSTscaleRatio)
            imgScale = cv.resize(img, (int(img.shape[1] * scaleRatio), int(img.shape[0] * scaleRatio)))
            cv.imwrite('myapp/static/myapp/images/' + name + '_scaled.jpg', imgScale)
            pathScaleRatio = name + '_scaled.jpg'
            # Image contrastEnhancement
            contrastEnhancement = float(POSTcontrastEnhancement)
            contrastEnhancementimg = cv.addWeighted(img, contrastEnhancement, np.zeros(img.shape, img.dtype), 0, 0)
            cv.imwrite('myapp/static/myapp/images/' + name + '_enhanced.jpg', contrastEnhancementimg)
            pathContrastEnhancement = name + '_enhanced.jpg'
            contrastEnhancement2 = float(POSTcontrastEnhancement)
            gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            # ubah  kedalaman 8-bit (CV_8UC1)
            gray_img = cv.convertScaleAbs(gray_img, alpha=contrastEnhancement2, beta=0)
            contrastEnhancement2img = cv.equalizeHist(gray_img, contrastEnhancement2)
            pathContrastEnhancement2 = name + '_enhanced2.jpg'
            cv.imwrite('myapp/static/myapp/images/' + name + '_enhanced2.jpg', contrastEnhancement2img)
            pathContrastEnhancement2 = name + '_enhanced2.jpg'
            # Image noiseReduction
            noiseReduction = bool(POSTnoiseReduction)
            if noiseReduction == True:
                imgnR = cv.GaussianBlur(contrastEnhancementimg, (5, 5), 0)
                imgnR2 = cv.GaussianBlur(contrastEnhancement2img, (5, 5), 0)
                cv.imwrite('myapp/static/myapp/images/' + name + '_noiseReduction.jpg', imgnR)
                pathNoiseReduction = name + '_noiseReduction.jpg'
                cv.imwrite('myapp/static/myapp/images/' + name + '_noiseReduction2.jpg', imgnR2)
                pathNoiseReduction2 = name + '_noiseReduction2.jpg'
            else:
                imgnR = contrastEnhancementimg
                pathNoiseReduction = name + '_enhanced.jpg'
                imgnR2 = contrastEnhancement2img
                pathNoiseReduction2 = name + '_enhanced2.jpg'
                
            XImage.objects.create(
                pathImage = name,
                uploader = POSTuploader,
                slug = name,
                contrastEnhancement = POSTcontrastEnhancement,
                dateCreated = datetime.now(),
                dateModified = datetime.now(),
                distanceObject = POSTdistanceObject,
                nameImage = POSTnameImage,
                noiseReduction = POSTnoiseReduction,
                scaleRatio = POSTscaleRatio,
                backgroundDominant = POSTbackgroundDominantColor,
                sizeImage = {
                    'width': width,
                    'height': height,
                    'channel': channels,
                    # dalam satuan mb
                    'size': os.path.getsize('myapp/static/myapp/images/' + name) / 1024 / 1024
                }
            )
            # Image Ground Truth
            ground_truth = ground_truth_image(imgnR)
            ground_truth2 = ground_truth_image(imgnR2)
            cv.imwrite('myapp/static/myapp/images/' + name + '_ground_truth.jpg', ground_truth)
            pathGroundTruth = name + '_ground_truth.jpg'
            cv.imwrite('myapp/static/myapp/images/' + name + '_ground_truth2.jpg', ground_truth2)
            pathGroundTruth2 = name + '_ground_truth2.jpg'
            
            ground_truth_noScale = ground_truth_image(img)
            ground_truth_noScale2 = ground_truth_image(imgnR2)
            print('ground_truth_noScale shape', ground_truth_noScale.shape)
            print('ground_truth_noScale2 shape', ground_truth_noScale2.shape)
            print('img shape', img.shape)
            kmeans_scores = kmeans_segmentation_scores(img, 2, scaleRatio, contrastEnhancement, ground_truth_noScale, ground_truth_noScale2)
            adaptive_scores = adaptive_threshold_segmentation_scores(img, 11, 2, scaleRatio, contrastEnhancement, ground_truth_noScale, ground_truth_noScale2)
            # Image segmentation using KMeans
            segKMeans = kmeans_segmentation(img, 2)
            cv.imwrite('myapp/static/myapp/images/' + name + '_segKMeans.jpg', segKMeans)
            pathKMeans = name + '_segKMeans.jpg'
            segKMeans2 = kmeans_segmentation(imgnR2, 2)
            cv.imwrite('myapp/static/myapp/images/' + name + '_segKMeans2.jpg', segKMeans2)
            pathKMeans2 = name + '_segKMeans2.jpg'
            # Image segmentation using Adaptive Thresholding
            segAdaptive = adaptive_threshold_segmentation(imgnR, 11, 2)
            cv.imwrite('myapp/static/myapp/images/' + name + '_segAdaptive.jpg', segAdaptive)
            pathAdaptive = name + '_segAdaptive.jpg'
            segAdaptive2 = adaptive_threshold_segmentation(imgnR2, 11, 2)
            cv.imwrite('myapp/static/myapp/images/' + name + '_segAdaptive2.jpg', segAdaptive2)
            pathAdaptive2 = name + '_segAdaptive2.jpg'
            # Image segmentation using Otsu's Thresholding
            segOtsu = otsu_threshold_segmentation(imgnR)
            cv.imwrite('myapp/static/myapp/images/' + name + '_segOtsu.jpg', segOtsu)
            pathOtsu = name + '_segOtsu.jpg'
            segOtsu2 = otsu_threshold_segmentation(imgnR2)
            cv.imwrite('myapp/static/myapp/images/' + name + '_segOtsu2.jpg', segOtsu2)
            pathOtsu2 = name + '_segOtsu2.jpg'
            # Image segmentation using Canny Edge Detection
            # find Treshold1 and Treshold2
            Treshold1 = int(np.median(imgnR) * 0.66)
            Treshold2 = int(np.median(imgnR) * 1.33)
            segCanny = canny_segmentation(imgnR, Treshold1, Treshold2)
            Treshold12 = int(np.median(imgnR2) * 0.66)
            Treshold22 = int(np.median(imgnR2) * 1.33)
            segCanny2 = canny_segmentation(imgnR2, Treshold12, Treshold22)
            cv.imwrite('myapp/static/myapp/images/' + name + '_segCanny.jpg', segCanny)
            pathCanny = name + '_segCanny.jpg'
            cv.imwrite('myapp/static/myapp/images/' + name + '_segCanny2.jpg', segCanny2)
            pathCanny2 = name + '_segCanny2.jpg'
            # Image segmentation using Sobel Edge Detection
            segSobel = sobel_segmentation(imgnR)
            segSobel2 = sobel_segmentation(imgnR2)
            cv.imwrite('myapp/static/myapp/images/' + name + '_segSobel.jpg', segSobel)
            pathSobel = name + '_segSobel.jpg'
            cv.imwrite('myapp/static/myapp/images/' + name + '_segSobel2.jpg', segSobel2)
            pathSobel2 = name + '_segSobel2.jpg'
            # Image segmentation using Prewitt Edge Detection
            segPrewitt = prewitt_segmentation(imgnR)
            segPrewitt2 = prewitt_segmentation(imgnR2)
            cv.imwrite('myapp/static/myapp/images/' + name + '_segPrewitt.jpg', segPrewitt)
            pathPrewitt = name + '_segPrewitt.jpg'
            cv.imwrite('myapp/static/myapp/images/' + name + '_segPrewitt2.jpg', segPrewitt2)
            pathPrewitt2 = name + '_segPrewitt2.jpg'
            
            
            # convert image segmentation from 2d to channel
            segAdaptive = cv.cvtColor(segAdaptive, cv.COLOR_GRAY2BGR)
            segOtsu = cv.cvtColor(segOtsu, cv.COLOR_GRAY2BGR)
            segAdaptive2 = cv.cvtColor(segAdaptive2, cv.COLOR_GRAY2BGR)
            segOtsu2 = cv.cvtColor(segOtsu2, cv.COLOR_GRAY2BGR)
            ground_truth2 = cv.cvtColor(ground_truth2, cv.COLOR_GRAY2BGR)
            segCanny2 = cv.cvtColor(segCanny2, cv.COLOR_GRAY2BGR)
            segSobel2 = segSobel2.astype(np.uint8)
            segSobel2 = cv.cvtColor(segSobel2, cv.COLOR_GRAY2BGR)
            segPrewitt2 = segPrewitt2.astype(np.uint8)
            segPrewitt2 = cv.cvtColor(segPrewitt2, cv.COLOR_GRAY2BGR)
            
            # convert the image segmented and ground truth to binary format (0 or 1)
            ground_truth[ground_truth > 0] = 1
            segKMeans[segKMeans > 0] = 1
            segAdaptive[segAdaptive > 0] = 1
            segOtsu[segOtsu > 0] = 1
            segCanny[segCanny > 0] = 1
            segSobel[segSobel > 0] = 1
            segPrewitt[segPrewitt > 0] = 1
            ground_truth2[ground_truth2 > 0] = 1
            segKMeans2[segKMeans2 > 0] = 1
            segAdaptive2[segAdaptive2 > 0] = 1
            segOtsu2[segOtsu2 > 0] = 1
            segCanny2[segCanny2 > 0] = 1
            segSobel2[segSobel2 > 0] = 1
            segPrewitt2[segPrewitt2 > 0] = 1

            # Calculate scores for segKMeans
            scores_kmeans = calculate_scores(ground_truth, segKMeans, 'kmeans')
            # print(scores_kmeans)
            # Calculate scores for segAdaptive
            scores_adaptive = calculate_scores(ground_truth, segAdaptive, 'adaptive')
            # print(scores_adaptive)
            # Calculate scores for segOtsu
            scores_otsu = calculate_scores(ground_truth, segOtsu, 'otsu')
            # print(scores_otsu)
            # Calculate scores for segCanny
            scores_canny = calculate_scores(ground_truth, segCanny, 'canny')
            # print(scores_canny)
            # Calculate scores for segSobel
            scores_sobel = calculate_scores(ground_truth, segSobel, 'sobel', 'weighted')
            # print(scores_sobel)
            # Calculate scores for segPrewitt
            scores_prewitt = calculate_scores(ground_truth, segPrewitt, 'prewitt')
            # print(scores_prewitt)
            # Calculate scores for segKMeans2
            scores_kmeans2 = calculate_scores(ground_truth2, segKMeans2, 'kmeans')
            # print(scores_kmeans2)
            # Calculate scores for segAdaptive2
            scores_adaptive2 = calculate_scores(ground_truth2, segAdaptive2, 'adaptive')
            # print(scores_adaptive2)
            # Calculate scores for segOtsu2
            scores_otsu2 = calculate_scores(ground_truth2, segOtsu2, 'otsu')
            # print(scores_otsu2)
            # Calculate scores for segCanny2
            scores_canny2 = calculate_scores(ground_truth2, segCanny2, 'canny')
            # print(scores_canny2)
            # Calculate scores for segSobel2
            scores_sobel2 = calculate_scores(ground_truth2, segSobel2, 'sobel', 'weighted')
            # print(scores_sobel2)
            # Calculate scores for segPrewitt2
            scores_prewitt2 = calculate_scores(ground_truth2, segPrewitt2, 'prewitt')
            # print(scores_prewitt2)
            # save scores to database
            
            XSegmentationResult.objects.create(
                pathPreprocessing = {
                    'pathPreprocessingOriginal': pathPreprocessingOriginal,
                    'pathScaleRatio': pathScaleRatio,
                    'pathContrastEnhancement': pathContrastEnhancement,
                    'pathContrastEnhancement2': pathContrastEnhancement2,
                    'pathNoiseReduction': pathNoiseReduction,
                    'pathNoiseReduction2': pathNoiseReduction2,
                    'pathGroundTruth': pathGroundTruth,
                    'pathGroundTruth2': pathGroundTruth2,
                },
                pathSegmentationResult = {
                    'pathKMeans': pathKMeans,
                    'pathKMeans2': pathKMeans2,
                    'pathAdaptive': pathAdaptive,
                    'pathAdaptive2': pathAdaptive2,
                    'pathOtsu': pathOtsu,
                    'pathOtsu2': pathOtsu2,
                    'pathCanny': pathCanny,
                    'pathCanny2': pathCanny2,
                    'pathSobel': pathSobel,
                    'pathSobel2': pathSobel2,
                    'pathPrewitt': pathPrewitt,
                    'pathPrewitt2': pathPrewitt2,
                },
                report = {
                    'kmeans_scores': kmeans_scores,
                    'adaptive_scores': adaptive_scores,
                    'scoresKMeans': scores_kmeans,
                    'scoresKMeans2': scores_kmeans2,
                    'scoresAdaptive': scores_adaptive,
                    'scoresAdaptive2': scores_adaptive2,
                    'scoresOtsu': scores_otsu,
                    'scoresOtsu2': scores_otsu2,
                    'scoresCanny': scores_canny,
                    'scoresCanny2': scores_canny2,
                    'scoresSobel': scores_sobel,
                    'scoresSobel2': scores_sobel2,
                    'scoresPrewitt': scores_prewitt,
                    'scoresPrewitt2': scores_prewitt2,
                },
                dateCreated = datetime.now(),
                dateModified = datetime.now(),
                idImage_id = XImage.objects.get(pathImage=name).id,
            )
        # redirect to image upload page
        return HttpResponseRedirect(reverse('myapp:imageUpload'))










