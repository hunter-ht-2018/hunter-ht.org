from django.conf.urls import url
from . import views
from Hunter_ht import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^signin/$',views.signin),
    url(r'^index/$',views.index),
    url(r'^admin/$',views.admin),
    url(r'^operator/$', views.operator),
    url(r'^upload/$',views.upload),
    url(r'^/static/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
