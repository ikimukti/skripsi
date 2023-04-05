from django.contrib import admin

# Register your models here.
from .models import XImage

class XImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'date', 'slug')

admin.site.register(XImage, XImageAdmin)

