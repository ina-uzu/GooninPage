from django.conf.urls import url

from main.views import add_post
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #Sign Up
    url(r'^join/$', views.signup, name='join'),

    #Sign in
    url(r'^login/$', views.signin, name ='login'),

    #Board-list
    url(r'^board/', views.show_post_list),

    #Board_write
    url(r'^board-write/', views.show_write_form),
    url(r'^add/', add_post),
    #Board read
    url(r'^board/(?P<pk>\d+)/', views.show_read_form),

    url(r'^schedule/', views.show_schd),

    url(r'^letters/', views.show_letters),
    url(r'^send/', views.send_letters),
]
