from django.urls import path, re_path
from . import views

app_name = 'services'
urlpatterns =[
    path('list', views.ServicesList.as_view(), name='list'),
    path('new', views.NewService.as_view(), name='new'),
    path('delete/<int:pk>/', views.delete_service, name='delete_service'),
]