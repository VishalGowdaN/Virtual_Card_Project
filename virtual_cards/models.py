from django.db import models

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid')
    ]
    invoice_number = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.status}"

class VirtualCard(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, unique=True)
    expiration_date = models.DateField()

    def __str__(self):
        return f"Card {self.card_number} for Invoice {self.invoice.invoice_number}"

class Transaction(models.Model):
    card = models.ForeignKey(VirtualCard, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction on {self.transaction_date} - {self.amount_paid}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.card.invoice.status = 'paid'
        self.card.invoice.save()