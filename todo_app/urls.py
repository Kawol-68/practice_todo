from django import urls
from django.urls import path, include
from .views import TodoList

urlpatterns = [
  path('list/', TodoList.as_view(), name='list')
]