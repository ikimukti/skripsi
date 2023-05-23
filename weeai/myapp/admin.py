from django.contrib import admin

# Register your models here.
from .models import XImage
from .models import XSegmentationResult

class XImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'dateCreated', 'dateModified', 'slug')

admin.site.register(XImage, XImageAdmin)

class XSegmentationResultAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'dateCreated', 'dateModified')

admin.site.register(XSegmentationResult, XSegmentationResultAdmin)

