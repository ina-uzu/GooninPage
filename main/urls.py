from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #Board-list
    url(r'^board/', views.show_post_list),

    #Board_write
    url(r'^board-write/', views.show_write_form),

    #Board read
    url(r'^board/(?P<pk>\d+)/', views.show_read_form),
] 
