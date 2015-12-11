from django.conf.urls import url
from homepage import views
# from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
]
