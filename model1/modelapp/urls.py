from django.urls import path
from . import views

urlpatterns = [
    path('modelapp/', views.modelapp, name='modelapp'),
]