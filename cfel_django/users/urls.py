from django.urls import path
from .views import loginView, log_outWiew

urlpatterns = [
    path('login', loginView, name='login'),
    path('logout', log_outWiew, name = 'logout')
]