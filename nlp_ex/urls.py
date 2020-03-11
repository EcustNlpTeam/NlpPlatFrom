from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import view, testdb, cloud, extract
from crawler import sina_news, weChat_account, create_task
from user import login, register
from show_pages import views

urlpatterns = [
    path('index/', views.index),
    path('text_titles/', views.text_title),
    path('text_content/', views.text_content),
    path('spread_wci/', views.spread_wci),
    path('crawler_form/', views.crawler_form),
    path('crawler_table/', views.crawler_table),
    path('user_defined/', views.user_defined),
    path('contact/', views.contact),
    url(r'^text_title$', views.text_title),
    url(r'^$',views.index),
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^cloud$', cloud.get_cloud),
    url(r'^summary$', extract.summary),
    url(r'^sina_news$', sina_news.get_pages),
    url(r'^login$', login.login),
    url(r'^logout$', login.logout),
    url(r'^register$', register.register),
    url(r'^weChat_account$', weChat_account.get_account),
    url(r'^create_task$', create_task.create_task),

]
