from django.conf.urls import url

from . import views

app_name = 'bookstore'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^insert_book/$', views.insert_book, name='insert_book'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^insert/$', views.insert_view, name='insert_view'),
    url(r'^update/$', views.update, name='update'),
    url(r'^update/action/$', views.action, name='action')
    # url(r'^update_view/$', views.update_view, name='update_view'),

]