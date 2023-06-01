from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('notice/new/', views.notice_new, name='notice_new'),
    path('notice/<int:pk>/edit/', views.notice_edit, name='notice_edit'),
]