from django.contrib import admin
from django.urls import path
from .views import webhook, send_message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/', webhook, name='webhook'),
    path('send/', send_message, name='send_message'),
]
