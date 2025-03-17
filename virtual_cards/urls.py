from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/create/', views.create_invoice, name='create_invoice'),
    path('virtual-cards/', views.virtual_card_list, name='virtual_card_list'),
    path('virtual-cards/create/', views.create_virtual_card, name='create_virtual_card'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/pay/', views.make_payment, name='make_payment'),
]