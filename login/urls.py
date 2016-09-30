from django.conf.urls import url

from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register_view, name='register_view'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^register_user/$',views.register_view,name='register_user'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^success/$', views.success, name='success')
]