from django.db import models
from users.models import Table as ut

# Create your models here.
class Table(models.Model):
    #CREATE TABLE IF NOT EXISTS product(
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    name = models.CharField(max_length=255) #VARCHAR(255) NOT NULL,
    def __str__(self):
        return self.name


