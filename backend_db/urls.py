"""URLS
for an specific app, in our case the db
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<int:pk>', views.room, name='room'),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
]