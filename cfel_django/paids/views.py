import datetime
import json


from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Table as pt, currency_sum, Money
from users.models import search_user_with_domain, sent_sanction_msg
from links.models import search_linked_id, linked_accounts
# Create your views here.

def paids_insert_minus(request):
    u_id = True
    url = '%2Fpaids%2Finsert%2Fminus'
    try:
        unkid = request.COOKIES['unkid']  
    except:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    user_info = search_user_with_domain(unkid)
    if user_info:
        who_value = ''
        sum_value = ''
        add_info_value = ''
        accounts = linked_accounts(user_info.users)
        accounts_name = list(map(lambda x: x.account, accounts))
        currency = Money.objects.filter(user = user_info.users)
        if request.method == 'POST':
            kredit = request.POST
            who_value = kredit['who']
            sum_value = kredit['kredit']
            add_info_value = kredit['add_info']
            # state = kredit['state']
            # print(state)

            if who_value and sum_value:
                today = datetime.date.today()
                u_id = search_linked_id(who_value, accounts)
                
                if u_id:
                    paids_table_insert = pt.objects.create(date = today, cash = sum_value, payer = user_info.users, taker = u_id, payer_comment = add_info_value, sanctioner = u_id, currency = currency_sum())
                    add_text = f'{u_id.account}. sizga {user_info.users.account} {sum_value} yubordi'
                    res = sent_sanction_msg('paids_table' ,paids_table_insert.id, user_info.users, u_id, sum_value, add_text, u_id)
                    return HttpResponseRedirect('minus')
                    
                
        data = {
            'accounts':accounts,
            'accounts_name': accounts_name ,
            'overall': currency[0].show_overall(),
            'who_linked':u_id, 
            'values':{'who_value':who_value,'sum_value':sum_value ,'add_info_value':add_info_value},
            'method': request.method,
            'state': 'minus',
            'user': user_info.users
            }
    else:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    
    return render(request, 'paids_insert.html', data)

def paids_insert_plus(request):
    u_id = True
    url = '%2Fpaids%2Finsert%2Fplus'
    try:
        unkid = request.COOKIES['unkid']  
    except:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    user_info = search_user_with_domain(unkid)
    if user_info:
        who_value = ''
        sum_value = ''
        add_info_value = ''
        accounts = linked_accounts(user_info.users)
        accounts_name = list(map(lambda x: x.account, accounts))
        currency = Money.objects.filter(user = user_info.users)
        if request.method == 'POST':
            kredit = request.POST
            who_value = kredit['who']
            sum_value = kredit['kredit']
            add_info_value = kredit['add_info']
            # state = kredit['state']
            # print(state)

            if who_value and sum_value:
                today = datetime.date.today()
                u_id = search_linked_id(who_value, accounts)
                
                if u_id:
                    paids_table_insert = pt.objects.create(date = today, cash = sum_value, payer = u_id, taker = user_info.users, payer_comment = add_info_value, sanctioner = u_id, currency = currency_sum())
                    add_text = f'{u_id.account}. sizdan {user_info.users.account} {sum_value} oldi'
                    res = sent_sanction_msg('paids_table' ,paids_table_insert.id, u_id, user_info.users, sum_value, add_text, u_id)
                    return HttpResponseRedirect('plus')
                    
                
        data = {
            'accounts':accounts,
            'accounts_name': accounts_name , 
            'overall': currency[0].show_overall(),
            'who_linked':u_id, 
            'values':{'who_value':who_value,'sum_value':sum_value ,'add_info_value':add_info_value},
            'method': request.method,
            'state': 'plus',
            'user': user_info.users
            }
    else:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    
    return render(request, 'paids_insert.html', data)

def cash_register(request):
    
    url = '%2Fpaids'
    try:
        unkid = request.COOKIES['unkid']  
    except:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    user_info = search_user_with_domain(unkid)
    data = {}
    if user_info:
        currency = Money.objects.filter(user = user_info.users)
        if currency:
            currency = currency[0]
            initial =  currency.show_initial()
            tables = currency.show_taker() | currency.show_payer()
            tables = tables.order_by('date', 'id')
            overall = currency.show_overall()
            data = {
                'initial': initial,
                'tables': tables,
                'overall': overall,
                'columns':['sana','kirim', 'chiqim', 'kimdan/kimga', "qo'shimcha"],
                'user': user_info.users
            }
    else:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    return render(request, 'paids_table.html', data)
    