from django.urls import path
from .views import HomView,MenuItemView,OrderView,casa
urlpatterns = [
    path('',HomView.as_view(),name='home'),
    path('menu/',MenuItemView.as_view(),name='menu'),
    path('orders/',OrderView.as_view(),name='order'),
    path('menu/casa/',casa,name='casa'),
]