from django.urls import path
from .views import HomePageView,BlogDetailView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/',BlogDetailView.as_view(), name='blog_detail'),
]