from django import forms
from .models import Invoice, VirtualCard, Transaction

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'amount']

class VirtualCardForm(forms.ModelForm):
    class Meta:
        model = VirtualCard
        fields = ['invoice', 'card_number', 'expiration_date']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['card', 'amount_paid']