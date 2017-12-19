from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.board_list, name='board_list'),
    url(r'^(?P<id>\d+)/$', views.board_detail, name='board_detail'),
    url(r'^new/$', views.board_new, name='board_new'),
]
