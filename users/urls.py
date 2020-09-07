from django.urls import path

from users import views

urlpatterns = [
    path('join/', views.join, name='join')
]