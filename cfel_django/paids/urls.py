from django.urls import path
from .views import paids_insert_minus, paids_insert_plus, cash_register

urlpatterns = [
    path('insert/plus', paids_insert_plus, name='paids_insert_plus'),
    path('insert/minus', paids_insert_minus, name='paids_insert_minus'),
    path('', cash_register, name='cash_register')
]
