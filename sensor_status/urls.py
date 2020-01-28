from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$',views.index, name='index'),   
     url(r'^(?P<sensor_id>[0-9]+)/$', views.feature, name= 'feature' ),
     url(r'^graph_simple_path.png', views.graph, name='graph')
          ]

