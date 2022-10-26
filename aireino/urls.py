"""aireino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from club.views import index,about,home,vayuyana,departments,events

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index.html',),
    path('about',about,name='about'),
    path('home',home,name='home'),
    path('departments',departments,name="departments"),
    path('events',events,name='events'),
    path('vayuyana',vayuyana,name='vayuyana'),
    path('',vayuyana,name='vayuyana.png'),
    path('',home,name='hoverpod.png'),
    path('',home,name="wrightflight.png"),
    path('',index,name='hoverpod.png'),
    path('',index,name="wrightflight.png"),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
    static(settings.STATIC_URL,document_root=settings.STATIC_ROOT),
  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

]

