from django.urls import path

from . import views

urlpatterns = [
    path('', views.create),
    path('/<uuid:tableId>', views.show),
    path('/<uuid:tableId>/players', views.create_player),
    path('/<uuid:tableId>/me', views.player_session),
]
