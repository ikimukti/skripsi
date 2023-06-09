from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUpClassView.as_view(), name="signup"),
    path("signout/", views.SignOutClassView.as_view(), name="signout"),
    path("signin/", views.SignInClassView.as_view(), name="signin"),
    path("setting/", views.SettingClassView.as_view(), name="setting"),
    path(
        "report/summary/", views.ReportSummaryClassView.as_view(), name="reportSummary"
    ),
    path(
        "report/segmentation/",
        views.ReportSegmentationClassView.as_view(),
        name="reportSegmentation",
    ),
    path(
        "report/export/report/",
        views.ReportExportReportClassView.as_view(),
        name="reportExportReport",
    ),
    path(
        "report/export/image/",
        views.ReportExportImageClassView.as_view(),
        name="reportExportImage",
    ),
    path("report/", views.ReportClassView.as_view(), name="report"),
    path(
        "preference/setting/",
        views.PreferenceSettingClassView.as_view(),
        name="preferenceSetting",
    ),
    path("preference/", views.PreferenceClassView.as_view(), name="preference"),
    path("modal/", views.modal, name="modal"),
    path("manage/user/", views.ManageUserClassView.as_view(), name="manageUser"),
    path("manage/role/", views.ManageRoleClassView.as_view(), name="manageRole"),
    path(
        "manage/permission/",
        views.ManagePermissionClassView.as_view(),
        name="managePermission",
    ),
    path("manage/group/", views.ManageGroupClassView.as_view(), name="manageGroup"),
    path("manage/", views.ManageClassView.as_view(), name="manage"),
    path("image/upload/", views.ImageUploadClassView.as_view(), name="imageUpload"),
    path(
        "image/uploader/<str:uploader>/",
        views.ImageUploaderClassView.as_view(),
        name="imageUploader",
    ),
    path(
        "image/summary/<int:id>/",
        views.ImageSummarySingleClassView.as_view(),
        name="imageSummarySingle",
    ),
    path("image/summary/", views.ImageSummaryClassView.as_view(), name="imageSummary"),
    path("image/manage/", views.ImageManageClassView.as_view(), name="imageManage"),
    path("image/list/", views.ImageListClassView.as_view(), name="imageList"),
    path("image/<int:id>/", views.ImageSingleClassView.as_view(), name="imageSingle"),
    path("image/", views.ImageClassView.as_view(), name="image"),
    path("help/", views.HelpClassView.as_view(), name="help"),
    path("docs/", views.DocsClassView.as_view(), name="docs"),
    path("dashboard/", views.DashboardClassView.as_view(), name="dashboard"),
    path("contact/", views.ContactClassView.as_view(), name="contact"),
    path("blog/", views.BlogClassView.as_view(), name="blog"),
    path(
        "account/profile/",
        views.AccountProfileClassView.as_view(),
        name="accountProfile",
    ),
    path(
        "account/change-password/",
        views.AccountChangePasswordClassView.as_view(),
        name="accountChangePassword",
    ),
    path("account/", views.AccountClassView.as_view(), name="account"),
    path("about/", views.AboutClassView.as_view(), name="about"),
    path("", views.IndexClassView.as_view(), name="index"),
]
