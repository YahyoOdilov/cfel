from itertools import product
from django.contrib import admin

from .models import Table, Product, Productioner, Add_values
# Register your models here.

admin.site.register(Table)
admin.site.register(Product)
admin.site.register(Productioner)
admin.site.register(Add_values)