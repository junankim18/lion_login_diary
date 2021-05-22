from django.contrib import admin
from django.urls import path, include
from diary.views import *


app_name = 'diary'

urlpatterns = [
    path('', diary_main, name='diary_main'),
    path('diary/', diary_list, name='diary_list'),
    path('diary/<int:pk>/', diary_detail, name='diary_detail'),
    path('diary/create/', diary_create, name='diary_create'),
    path('diary/<int:pk>/update', diary_update, name='diary_update'),
    path('diary/<int:pk>/delete', diary_delete, name='diary_delete'),
]
