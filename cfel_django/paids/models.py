from locale import currency
from turtle import pu
from django.db import models
from django.db.models import Sum
from users.models import Table as ut
from additional import put_comma

# Create your models here.
class Currency(models.Model):
    what = models.CharField(max_length=255)

    def __str__(self):
        return self.what

class Money(models.Model):
    date = models.CharField(max_length=255)
    currency = models.ForeignKey(Currency, models.CASCADE, null=True)
    user = models.ForeignKey(ut, models.CASCADE, null=True)
    initial = models.FloatField()
    def __str__(self):
        return f'{self.date} - {self.currency.what} - {self.user.account} - {self.initial} - {self.overall}' 
    def show_initial(self):
        return self.initial
    def show_payer(self):
        return Table.objects.filter(payer = self.user, currency = self.currency).all()
    def show_taker(self):
        return Table.objects.filter(taker = self.user, currency = self.currency).all()
    def show_overall(self):
        payers = Table.objects.filter(payer = self.user, currency = self.currency).all().aggregate(Sum('cash'))
        taker = Table.objects.filter(taker = self.user, currency = self.currency, sanction = True).all().aggregate(Sum('cash'))
        cash_payer = payers['cash__sum'] if payers['cash__sum'] else 0
        cash_taker = taker['cash__sum'] if taker['cash__sum'] else 0

        return put_comma(self.initial - cash_payer + cash_taker)

class Table(models.Model):
    # CREATE TABLE IF NOT EXISTS paids(
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    date = models.CharField(max_length=255) #VARCHAR(255) NOT NULL,
    currency = models.ForeignKey(Currency, models.CASCADE, null=True)
    cash = models.FloatField() #BIGINT NOT NULL,
    payer = models.ForeignKey(ut, on_delete=models.CASCADE, related_name='payer+') #BIGINT NOT NULL,
    taker = models.ForeignKey(ut, on_delete=models.CASCADE, related_name='taker+') #BIGINT NOT NULL,
    sanctioner = models.ForeignKey(ut, on_delete=models.CASCADE, related_name='sanctioner+', null=True)
    diliver_paid = models.FloatField(null=True) #BIGINT,
    sanction = models.BooleanField(null=True) #BOOLEAN,
    sanction_date = models.CharField(max_length=255, null=True) #VARCHAR(255),
    payer_comment = models.CharField(max_length=255, null=True) #VARCHAR(255),
    taker_comment = models.CharField(max_length=255, null=True) #VARCHAR(255)

    def __str__(self):
        return f'(id:{self.id}) - (date:{self.date}) - (payer-id:{self.payer.account}) - (taker-id:{self.taker.account}) - (sanction:{self.sanction}) '
    def show_cash(self):
        return put_comma(self.cash)
    
def currency_sum():
    return Currency.objects.all()[0]