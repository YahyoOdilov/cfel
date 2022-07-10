import datetime
import json



from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse

from users.models import Table as ut, User_domains, search_user_with_domain, sent_sanction_msg
from links.models import search_linked_id, linked_accounts
from .models import Product, Table as st, Storage, search_product, test_product, producter_show, provider_show, storages_show

# Create your views here.
def sents_insert_minus(request):
    url = '%2Fsents%2Finsert%2Fminus'
    try:
        unkid = request.COOKIES['unkid']  
    except:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    user_info = search_user_with_domain(unkid)
    if user_info:
        products = search_product(user_info.users)
        accounts = linked_accounts(user_info.users)
        accounts_name = list(map(lambda x: x.account, accounts))
        products_name = list(map(lambda x: x.product.name, products))
        
        if request.method == 'POST':
            request_data = request.POST
            who_value = request_data['who']
            add_info_value = request_data['addinfo']
            table = json.loads(request_data['table'])
            if who_value:
                today = datetime.date.today()
                u_id = search_linked_id(who_value, accounts)
                if u_id:
                    overall = 0
                    table_insert = st.objects.create(date = today, provider = user_info.users, producter = u_id, provider_comment = add_info_value, sanctioner = u_id)
                    for_add_text = ''
                    for back_product in table:
                        product_table = test_product(back_product['product'], user_info.users)
                        is_there_product = test_product(back_product['product'], u_id)
                        if not is_there_product:
                            create_storage = Storage.objects.create(date = today, product = product_table.product, user = u_id, initial = 0)
                        if product_table:
                            insert_product = Product.objects.create(product = product_table.product, product_value = back_product['product_value'], product_price = back_product['product_price'], production = table_insert)
                            product_overall = float(back_product['product_value']) * float(back_product['product_price'])
                            overall += product_overall                                
                            for_add_text += f'{product_table.product.name}:{back_product["product_value"]} - {back_product["product_price"]}dan {product_overall}\n'
                    add_text = f'{u_id.account}. sizga {user_info.users.account} {overall}lik hizmat yoki mahsulot yubordi \n\n {for_add_text}'
                    insert_overall = st.objects.filter(id = table_insert.id).update(overall = overall)
                            
                            
                    res = sent_sanction_msg('sents_table' ,table_insert.id, user_info.users, u_id, overall, add_text, u_id)
                    return HttpResponse(json.dumps('/sents/insert/minus'))
                               
        data = {
            'accounts': json.dumps(accounts_name),
            'products': json.dumps(products_name),
            'state':'minus',
            'user': user_info.users
            }

    else:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    return render(request, 'sents_insert.html', data)

def sents_insert_plus(request):
    url = '%2Fsents%2Finsert%2Fplus'
    try:
        unkid = request.COOKIES['unkid']  
    except:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    user_info = search_user_with_domain(unkid)
    if user_info:
        products = search_product(user_info.users)
        
        accounts = linked_accounts(user_info.users)
        accounts_name = list(map(lambda x: x.account, accounts))

        
        if request.method == 'POST':
            request_data = request.POST
            who_value = request_data['who']
            add_info_value = request_data['addinfo']
            table = json.loads(request_data['table'])
            if who_value:
                today = datetime.date.today()
                u_id = search_linked_id(who_value, accounts)
                if u_id:
                    overall = 0
                    table_insert = st.objects.create(date = today, provider =u_id, producter = user_info.users, producter_comment = add_info_value, sanctioner = u_id )
                    for_add_text = ''
                    for back_product in table:
                        product_table = test_product(back_product['product'], u_id)
                        is_there_product = test_product(back_product['product'], user_info.users)
                        if not is_there_product:
                            create_storage = Storage.objects.create(date = today, product = product_table.product, user = user_info.users, initial = 0)
                        if product_table:
                            insert_product = Product.objects.create(product = product_table.product, product_value = back_product['product_value'], product_price = back_product['product_price'], production = table_insert)
                            product_overall = float(back_product['product_value']) * float(back_product['product_price'])
                            overall += product_overall                                
                            for_add_text += f'{product_table.product.name}:{back_product["product_value"]} - {back_product["product_price"]}dan {product_overall}\n'
                    add_text = f'{u_id.account}. sizdan {user_info.users.account} {overall}lik hizmat yoki mahsulot oldi \n\n {for_add_text}'
                    insert_overall = st.objects.filter(id = table_insert.id).update(overall = overall)
                            
                            
                    res = sent_sanction_msg('sents_table' ,table_insert.id, u_id, user_info.users, overall, add_text, u_id)
                    return HttpResponse(json.dumps('/sents/insert/plus'))
                               
        data = {
            'accounts': json.dumps(accounts_name),
            'products': json.dumps([]),
            'state': 'plus',
            'user': user_info.users
            }

    else:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    return render(request, 'sents_insert.html', data)

def product(request):
    account = request.GET['account']
    
    user = ut.objects.filter(account = account)[0]
    products = search_product(user)
    products = list(map(lambda x: x.product.name, products))
    return HttpResponse(json.dumps(products))

def sents_table(request):
    url = '%2Fsents'
    try:
        unkid = request.COOKIES['unkid']  
    except:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    user_info = search_user_with_domain(unkid)
    if user_info:
        producters_show = producter_show(user_info.users)
        providers_show = provider_show(user_info.users)
        tables = producter_show(user_info.users) | provider_show(user_info.users)
        tables = tables.order_by('date', 'id')
    else:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    
    data = {
                'tables': tables,
                'columns':['sana','kirim', 'chiqim', 'kimdan/kimga', "qo'shimcha"],
                'user': user_info.users
            }
    return render(request, 'sents_table.html', data)

def storage(request):
    url = '%2Fsents%2Fstorage'
    try:
        unkid = request.COOKIES['unkid']  
    except:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    user_info = search_user_with_domain(unkid)
    if user_info:
        storages = storages_show(user_info.users)
    else:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    
    data = {
                'tables': storages,
                'columns':['mahsulot', 'sklad'],
                'user': user_info.users
            }
    return render(request, 'storage_table.html', data)