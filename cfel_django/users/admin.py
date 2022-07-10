from django.contrib import admin

# Register your models here.

from .models import Table, Businesses, Diliver, Telegram_ids, User_domains

admin.site.register(Table)
admin.site.register(Businesses)
admin.site.register(Diliver)
admin.site.register(Telegram_ids)
admin.site.register(User_domains)