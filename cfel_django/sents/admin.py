from django.contrib import admin

# Register your models here.

from .models import Table, Product, Add_values, Bag_value, Loading, Storage

admin.site.register(Table)
admin.site.register(Product)
admin.site.register(Add_values)
admin.site.register(Bag_value)
admin.site.register(Loading)
admin.site.register(Storage)