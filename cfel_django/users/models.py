from django.db import models
import requests as re
import json

# Create your models here.
class Table(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=20)
    sure_name= models.CharField(max_length=255)# VARCHAR(255) NOT NULL,
    name= models.CharField(max_length=255) # VARCHAR(255) NOT NULL,
    tell_num = models.CharField(max_length=20) # VARCHAR(20) NOT NULL,
    type_work = models.CharField(max_length=20) # VARCHAR(20) NOT NULL,
    is_creator = models.BooleanField(null=True) # BOOLEAN,
    working_with = models.BigIntegerField(null=True) #BIGINT

    def __str__(self):
        return f'(id:{self.id}) - (account:{self.account}) - (is-creator:{self.is_creator}) - (fullname:{self.name} {self.sure_name})'

class Businesses(models.Model):
    #CREATE TABLE IF NOT EXISTS businesses(
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    users_id = models.BigIntegerField() #BIGINT NOT NULL,
    business_name = models.CharField(max_length=255) # VARCHAR(255),
    latitude = models.FloatField(null=True) #BIGINT NOT NULL,
    longitude = models.BigIntegerField(null=True) #BIGINT NOT NULL

    def __str__(self):
        return f'(id:{self.id}) - (business:{self.business_name}) - (location:{self.longitude}:{self.latitude}) - (user-id:{self.users_id})'

class Diliver(models.Model):
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    users_id = models.BigIntegerField() #BIGINT NOT NULL,
    avto_num = models.CharField(max_length=255) #VARCHAR(255),

    def __str__(self):
        return f'(id:{self.id}) - (avto-num:{self.avto_num}) - (user_id:{self.users_id})' 

class Telegram_ids(models.Model):
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY AUTOINCREMENT,
    telegram_id = models.BigIntegerField() #BIGINT NOT NULL,
    users = models.ForeignKey(Table, on_delete=models.CASCADE) #BIGINT NOT NULL,
    is_active = models.BooleanField(null=True) #BOOLEAN NOT NULL
    def __str__(self):
        return f'(id:{self.id}) - (telegram-id:{self.telegram_id}) - (user-id:{self.users.account})'

class User_domains(models.Model):
    user_domain = models.CharField(max_length=255)
    users = models.ForeignKey(Table, on_delete=models.CASCADE)
    is_active = models.BooleanField(null=True)
    def __str__(self):
        name = {'user_domain':self.user_domain, 'user_id': self.users.account}
        return f'{name}'



#to take info from models
def sent_sanction_msg(table, table_id, payer, taker, sum, text, sanctioner):
        t_ids = list(filter(lambda x: x.users == sanctioner , Telegram_ids.objects.all() ))
        button = json.dumps({"inline_keyboard":[[{"text":"tasdiqlash","callback_data":json.dumps(['for_action', table, table_id, payer.id, taker.id, sum])}]]})
        for t_id in t_ids:
            return re.get(f'https://api.telegram.org/bot2124160021:AAGO-VHtWikQ3HVS6OI-o0dJMl5Fj0-Csmc/sendMessage?chat_id={t_id.telegram_id}&text={text}&reply_markup={button}')

def search_user_with_domain(unkid):
    result = []
    user_info = User_domains.objects.filter(user_domain = unkid).all()
    if user_info: result = user_info[0]
    return result