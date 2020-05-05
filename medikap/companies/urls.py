from django.urls import path, re_path
from . import views

app_name = 'companies'
urlpatterns =[
    path('list', views.CompanyList.as_view(), name='list'),
    path('new', views.NewCompany.as_view(), name='new'),
    re_path(r'^detail/(?P<company_id>\d+)/$', views.DetailsCompany.as_view(), name='detail'),
]