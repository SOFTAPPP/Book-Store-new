from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('sale/', views.sale_page, name="sale_page"),
]