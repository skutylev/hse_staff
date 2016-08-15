#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get/', views.get_list_cals),
    url(r'^events/create/', views.create_event),
    url(r'^events/cancel/', views.cancel_event),
    url(r'^events/get/', views.get_list_events)
]
