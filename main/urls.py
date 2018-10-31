from django.conf.urls import url

from main.views import add_post
from . import views

urlpatterns = [
    # Sign in
    url(r'^$', views.signin, name='login'),

    #Sign Up
    url(r'^join/$', views.signup, name='join'),

    #main
    url(r'^main$', views.index, name='index'),

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
