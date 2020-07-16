from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('blogger/<int:pk>/', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),

    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
]