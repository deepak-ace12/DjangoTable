from django.conf.urls import url
from . import views

#app_name = 'music'
urlpatterns = [

    #/batch/
    url(r'^$', views.index, name='index'),

    #/batch/id
    url(r'^(?P<batch_id>[0-9]+)/$', views.batch_students, name = 'batch_students'),
]
