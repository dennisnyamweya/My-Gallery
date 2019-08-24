from django.conf.urls import url
from . import views

#url patterns
urlpatterns = [
    url(r'^$', views.picture_list,name='picture_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.picture_list,name='picture_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.picture_detail,name='picture_detail'),
]