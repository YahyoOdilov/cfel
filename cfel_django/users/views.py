import json
from uuid import uuid5
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from uuid import uuid4
# Create your views here.

from.models import Table
from .models import User_domains, search_user_with_domain
def loginView(request):
    url = ''
    try:
        url = request.GET['url']
    except:
        pass
    try:
        unkid = request.COOKIES['unkid']  
        user = search_user_with_domain(unkid).id
        return HttpResponseRedirect(f'/..')
    except:
        pass
    account = ''
    password = ''
    u_info = True
    if request.method == 'POST':
        post_data = request.POST
        account = post_data['account']
        password = post_data['password']
        if account and password:
            u_info = Table.objects.filter(account = account, password = password)
            if u_info:
                unkid = uuid4()
                ud_table = User_domains.objects.create(users = u_info[0], user_domain = unkid, is_active = True)
                response = HttpResponseRedirect(f'/..{url}')
                response.set_cookie('unkid', unkid)
                return response



    return render(request, 'loginpage.html', {'account':account, 'password': password, 'method':request.method, 'isLinked': u_info, 'url':url,'user':0})

def log_outWiew(request):
    try:
        unkid = request.COOKIES['unkid']  
    except:
        return HttpResponseRedirect(f'/../users/login')
    user_info = search_user_with_domain(unkid)
    
    if user_info:
        user_info.delete()
        response = HttpResponseRedirect(f'/../users/login')
        response.delete_cookie('unk')
        return response
    else:
        return HttpResponseRedirect(f'/../users/login')