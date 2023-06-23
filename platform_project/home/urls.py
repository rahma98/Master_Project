# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:40:06 2023

@author: PC GAMER
"""

from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('features', views.features, name='features'),
    path('about', views.about, name='about'),
    path('history', views.history, name='history'),
    path('statics', views.statics, name='statics'),
    path('eda_1', views.eda_1, name='eda_1'),
    path('eda_2', views.eda_2, name='eda_2'),
    path('eda_3', views.eda_3, name='eda_3'),
    path('eda_4', views.eda_4, name='eda_4'),
    path('eda_5', views.eda_5, name='eda_5'),
    path('eda_6', views.eda_6, name='eda_6')
    
    
]