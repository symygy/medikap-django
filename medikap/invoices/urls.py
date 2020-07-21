from django.urls import path, re_path
from . import views

app_name = 'invoices'
urlpatterns =[
    path('list', views.InvoiceList.as_view(), name='list'),
    path('new', views.NewInvoice.as_view(), name='new'),
    re_path(r'^detail/(?P<invoice_id>\d+)/$', views.DetailsInvoice.as_view(), name='detail'),
    path('delete/<int:pk>', views.DeleteInvoice.as_view(), name='delete'),
    #test

]