from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listado, name='listado'),
    url(r'^registrar$', views.registrar, name='registrar'),
    
]