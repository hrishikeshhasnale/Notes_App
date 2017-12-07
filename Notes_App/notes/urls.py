"""Notes_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mynotes/$', views.mynotes, name = 'mynotes'),
    url(r'^s_notes/$', views.s_notes, name = 's_notes'),
    url(r'^update_nt/$', views.update_nt, name = 'update_nt'),
    url(r'^update_note/$', views.update_note, name = 'update_note'),
    url(r'^del_note/$', views.del_note, name = 'del_note'),
    url(r'^view_note/$', views.view_note, name = 'view_note'),
    url(r'^shared/$', views.shared, name = 'shared')
]
