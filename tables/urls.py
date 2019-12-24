from django.urls import path

from . import views

urlpatterns = [
    path('', views.create),
    path('/<str:tableId>/players', views.create_player),
]
