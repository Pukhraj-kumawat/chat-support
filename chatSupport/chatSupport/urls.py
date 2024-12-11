from django.contrib import admin
from django.urls import path
from .views import webhook, send_message,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('webhook', webhook, name='webhook'),
    path('send', send_message, name='send_message'),
]
