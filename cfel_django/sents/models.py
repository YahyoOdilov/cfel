from turtle import pu
from django.db import models
from users.models import Table as ut
from product.models import Table as prt
from django.db.models import Sum
from additional import put_comma

# Create your models here.

class Storage(models.Model):
    date = models.CharField(max_length=255)
    product = models.ForeignKey(prt, models.CASCADE)
    user = models.ForeignKey(ut, models.CASCADE)
    initial = models.FloatField()
    def __str__(self):
        return self.user.account + ' - ' + self.product.name
    
    def show_initial(self):
        return self.initial
    def show_overall(self):
        producters_table = Product.objects.filter(product = self.product, production__producter = self.user).all()
        providers_table = Product.objects.filter(product = self.product, production__provider = self.user).all()
        producters_table_no_san = producters_table.filter(production__sanctioner = self.user, production__sanction = True)
        producters_table_san = producters_table.exclude(production__sanctioner = self.user )
        providers_table_no_san = providers_table.filter(production__sanctioner = self.user, production__sanction = True)
        providers_table_san = providers_table.exclude(production__sanctioner = self.user )
        all_producter = producters_table_san | producters_table_no_san
        all_provider = providers_table_san | providers_table_no_san
        sum_producter = 0 if not all_producter.aggregate(Sum('product_value'))['product_value__sum'] else all_producter.aggregate(Sum('product_value'))['product_value__sum']
        sum_provider = 0 if not all_provider.aggregate(Sum('product_value'))['product_value__sum'] else all_provider.aggregate(Sum('product_value'))['product_value__sum']
        result = self.initial + sum_producter - sum_provider
        return put_comma(result)
        

class Table(models.Model):
    #CREATE TABLE IF NOT EXISTS sents(
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    date = models.CharField(max_length=255) #VARCHAR(255) NOT NULL,
    production_id = models.BigIntegerField(null=True) #BIGINT,
    producter = models.ForeignKey(ut, on_delete=models.CASCADE, related_name= 'producter+' ,null=True) #BIGINT NOT NULL,
    provider = models.ForeignKey(ut, on_delete=models.CASCADE, related_name='provider+' ,null=True) #BIGINT NOT NULL,
    sanction = models.BooleanField(null=True) #BOOLEAN,
    sanction_date = models.CharField(max_length=255, null=True) #VARCHAR(255),
    sanctioner = models.ForeignKey(ut, on_delete=models.CASCADE, related_name='sanctioner+', null=True)
    producter_comment = models.CharField(max_length=255, null=True) #VARCHAR(255),
    provider_comment = models.CharField(max_length=255, null=True) #VARCHAR(255),
    overall = models.FloatField(null=True) #BIGINT

    def show_overall(self):
        return put_comma(self.overall)
    def __str__(self):
        return f'(id:{self.id}) - (date:{self.date}) - (provider-id:{self.provider_id}) - (producter-id:{self.producter_id}) - (sanction:{self.sanction}) - (overall:{self.overall})'
    def sents_products(self):
        products = Product.objects.filter(production = self).all()
        return products

class Loading(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=255)
    fuller_in_id = models.BigIntegerField()
    sents_id = models.BigIntegerField(null=True)
    overall = models.BigIntegerField(null=True)
    sanction = models.BooleanField(null=True)
    sanction_date = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f'id:{self.id} - date:{self.date} - fuller-in-id:{self.fuller_in_id} - sents-id:{self.sents_id} - sanction:{self.sanction} - overall:{self.overall}'
    
class Product(models.Model):
    #CREATE TABLE IF NOT EXISTS product(
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    product = models.ForeignKey(prt, on_delete=models.PROTECT, related_name='storage+') #BIGINT NOT NULL,
    product_value = models.FloatField() #BIGINT NOT NULL,
    product_price = models.FloatField(null=True) #BIGINT NOT NULL
    production = models.ForeignKey(Table,models.CASCADE) #BIGINT NOT NULL

    def show_value(self):
        return put_comma(self.product_value)
    def show_price(self):
        return put_comma(self.product_price)
    def __str__(self):
        return f'(id:{self.id}) - (product-id:{self.product_id}) - (product-value:{self.product_value})  - (product-price:{self.product_price}) - (orders-id:{self.production_id})'


class Add_values(models.Model):
    #CREATE TABLE IF NOT EXISTS add_values(
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    value = models.BigIntegerField() #BIGINT NOT NULL,
    reason_add = models.CharField(max_length=255) #VARCHAR(255) NOT NULL,
    production_id = models.BigIntegerField() #BIGINT NOT NULL

    def __str__(self):
        return f'(id:{self.id}) - (value:{self.value}) - (reason-add:{self.reason_add}) - (production-id:{self.production_id}) '

class Bag_value(models.Model):
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    product_id = models.BigIntegerField() #BIGINT NOT NULL,
    product_value = models.BigIntegerField() #BIGINT NOT NULL,
    loading_paid = models.BigIntegerField(null=True) #BIGINT NOT NULL,
    production_id = models.BigIntegerField() #BIGINT NOT NULL

    def __str__(self):
        return f'id:{self.id} - product_id:{self.product_id} - product_value:{self.product_value} loading-paid:{self.loading_paid} production_id:{self.production_id}'

#to take info from models
def search_product(user):
    result = Storage.objects.filter(user = user).all()
    return result

def test_product(product, user):
    products = search_product(user)
    result = list(filter(lambda x: x.product.name == product, products))
    if result: result = result[0]
    return result

def provider_show(user):
    provider = Table.objects.filter(provider = user).all()
    return provider
def producter_show(user):
    producter = Table.objects.filter(producter = user).all()
    return producter
def storages_show(user):
    storages = Storage.objects.filter(user = user).all()
    return storages

