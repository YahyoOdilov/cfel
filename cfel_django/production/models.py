from django.db import models

# Create your models here.

# Create your models here.
class Table(models.Model):
    #CREATE TABLE IF NOT EXISTS sents(
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    date = models.CharField(max_length=255) #VARCHAR(255) NOT NULL,
    fuller_id = models.BigIntegerField()
    company_id = models.BigIntegerField(null=True) #BIGINT,
    sanctioner_id = models.BigIntegerField() #BIGINT NOT NULL,
    sanction = models.BooleanField(null=True) #BOOLEAN,
    sanction_date = models.CharField(max_length=255, null=True) #VARCHAR(255),
    productioner_comment = models.CharField(max_length=255, null=True) #VARCHAR(255),
    sanctioner_comment = models.CharField(max_length=255, null=True) #VARCHAR(255),
    overall = models.BigIntegerField(null=True) #BIGINT

    def __str__(self):
        return f'(id:{self.id}) - (date:{self.date}) - (fuller-id:{self.fuller_id}) - (sactioner-id:{self.sanctioner_id}) - (sanction:{self.sanction}) - (overall:{self.overall})'
    
class Product(models.Model):
    #CREATE TABLE IF NOT EXISTS product(
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    product_id = models.BigIntegerField() #BIGINT NOT NULL,
    product_value = models.BigIntegerField() #BIGINT NOT NULL,
    product_price = models.BigIntegerField() #BIGINT NOT NULL
    production_id = models.BigIntegerField() #BIGINT NOT NULL

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


class Productioner(models.Model):
    id = models.BigAutoField(primary_key=True)
    worker_id= models.BigIntegerField()
    value = models.BigIntegerField()
    production_id = models.BigIntegerField()
    production_sanction = models.BooleanField(null=True)
    production_sanction_date = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'(id:{self.id}) - (worker-id:{self.worker_id}) - (value:{self.value}) - (sanction:{self.production_sanction}) '