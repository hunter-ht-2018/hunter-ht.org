from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^signin/$',views.signin),
    url(r'^index/$',views.index),
    url(r'^register/$',views.register),
]
