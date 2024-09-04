from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('modelapp/', views.modelapp, name='modelapp'),
    path('modelapp/details/<int:id>/', views.details, name='details'),
]