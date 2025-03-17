from django.shortcuts import render, redirect
from .models import Invoice, VirtualCard, Transaction
from .forms import InvoiceForm, VirtualCardForm, TransactionForm

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'virtual_cards/invoice_list.html', {'invoices': invoices})

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'virtual_cards/invoice_form.html', {'form': form})

def virtual_card_list(request):
    cards = VirtualCard.objects.all()
    return render(request, 'virtual_cards/virtual_card_list.html', {'cards': cards})

def create_virtual_card(request):
    if request.method == 'POST':
        form = VirtualCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('virtual_card_list')
    else:
        form = VirtualCardForm()
    return render(request, 'virtual_cards/virtual_card_form.html', {'form': form})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'virtual_cards/transaction_list.html', {'transactions': transactions})

def make_payment(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'virtual_cards/transaction_form.html', {'form': form})