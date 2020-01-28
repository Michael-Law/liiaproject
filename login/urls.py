from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$',views.login_access, name='login_access'),   
               ]