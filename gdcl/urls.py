from django.conf.urls import url
from . import views

app_name = 'gdcl_index'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^works/$', views.works, name='works'),
    url(r'^description/$', views.description, name='description'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^infomation/$', views.infomation, name='infomation'),
    url(r'^culture/$', views.culture, name='culture'),
    url(r'^organization/$', views.organization, name='organization'),
    url(r'^certification/$', views.certification, name='certification'),
    url(r'^reputation/$', views.reputation, name='reputation'),
]