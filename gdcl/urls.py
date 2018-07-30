from django.conf.urls import url
from . import views

app_name = 'gdcl'
urlpatterns = [
    # 首页
    url(r'^$', views.index, name='index'),

    # 企业概况五个
    url(r'^description/$', views.description, name='description'),
    url(r'^boss/$', views.boss, name='boss'),
    url(r'^organization/$', views.organization, name='organization'),
    url(r'^certification/$', views.certification, name='certification'),
    url(r'^reputation/$', views.reputation, name='reputation'),

    # 企业文化五个
    url(r'^logo/$', views.logo, name='logo'),
    url(r'^management/$', views.management, name='management'),
    url(r'^show/$', views.show, name='show'),
    url(r'^video/$', views.video, name='video'),
    url(r'^employee/$', views.employee, name='employee'),

    # 工程业绩三个
    url(r'^rewards/$', views.rewards, name='rewards'),
    url(r'^project_show/$', views.project_show, name='project_show'),
    url(r'^project_photo/$', views.project_photo, name='project_photo'),

    # 新闻资讯四个
    url(r'^company_news/$', views.company_news, name='company_news'),
    url(r'^movement/$', views.movement, name='movement'),
    url(r'^note/$', views.note, name='note'),
    url(r'^others/$', views.others, name='others'),

    # 关于我们两个
    url(r'^recruitment/$', views.recruitment, name='recruitment'),
    url(r'^contact/$', views.contact, name='contact'),

    #
]