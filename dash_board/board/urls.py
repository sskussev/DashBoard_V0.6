from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .dash_apps.finished import map
from .dash_apps.finished import without_vpn
from .dash_apps.finished import without_vpn_mts
from .dash_apps.finished import without_vpn_tele2
from .dash_apps.finished import without_vpn_mgts
from .dash_apps.finished import without_vpn_beeline
from .dash_apps.finished import without_vpn_megafon
from .dash_apps.finished import without_vpn_rostelecom
from .dash_apps.finished import without_vpn_rostelecom_mobile
from .dash_apps.finished import dynamic_graph
from .dash_apps.finished import dynamic_graph_table
# from .dash_apps.finished import asn_data


app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('analytics/', views.analytics, name='analytics'),
    path('file/<str:filename>/', views.download_file, name='download_file'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)