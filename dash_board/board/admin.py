# from django.contrib import admin
#
# from .models import DownloadFiles
#
#
# class DownloadFilesAdmin(admin.ModelAdmin):
#     list_display = ('file_name',
#                     'author',
#                     'created',
#                     )
#     list_filter = ('created',)
#
#
# admin.site.register(DownloadFiles)

from django.contrib import admin

from .models import DownloadFiles


@admin.register(DownloadFiles)
class DownloadFilesAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'author', 'created',]