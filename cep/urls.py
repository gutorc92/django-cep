# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import addressGet

urlpatterns = [
               url(r'^(?P<zipcode>[\w-]+)/$', addressGet, name='address'),
              ]        
