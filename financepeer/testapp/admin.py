from django.contrib import admin
from testapp.models import Upload,DisplayItems
# Register your models here.

class UploadAdmin(admin.ModelAdmin):
    list_display=['file',]

admin.site.register(Upload,UploadAdmin)

class DisplayItemsAdin(admin.ModelAdmin):
    list_display=['userId','title','body']

admin.site.register(DisplayItems,DisplayItemsAdin)
