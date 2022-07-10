from django.urls import path
from .views import sents_insert_minus, sents_insert_plus, product, sents_table, storage

urlpatterns = [
    path('insert/plus', sents_insert_plus, name='sents_insert_plus'),
    path('insert/minus', sents_insert_minus, name = 'sents_insert_minus'),
    path('product/take', product , name='sents_insert'),
    path('', sents_table, name='sents_table'),
    path('storage', storage, name = 'storage')
]