from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('sale/', include('sale.urls')),
]