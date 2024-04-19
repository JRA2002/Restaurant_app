from django.urls import path
from .views import HomView
urlpatterns = [
    path('',HomView.as_view(),name='home')
]