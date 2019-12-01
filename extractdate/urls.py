from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [

    # url(r'^(?P<base64_string>.+)', views.date_extract,name='urlname')
    url('',views.home),
    url('date/',views.date_extract, name='output')
    
]
