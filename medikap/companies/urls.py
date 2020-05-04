from django.urls import path
from . import views

app_name = 'companies'
urlpatterns =[
    path('list', views.CompanyList.as_view(), name='list'),
    path('new', views.NewCompany.as_view(), name='new'),
]