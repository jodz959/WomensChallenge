from django.conf.urls import url, include
from home import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^groups/', views.groups, name='group'),

    url(r'^opportunities/$', views.opportunities, name='opportunities'),


    url(r'^mentor/$', views.mentor, name='mentor'),

    url(r'^user/$', views.user, name='user')

]
