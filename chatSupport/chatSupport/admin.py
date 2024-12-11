from django.contrib import admin
from .models import WhatsAppMessage

@admin.register(WhatsAppMessage)
class WhatsAppMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp', 'status')
    search_fields = ('sender', 'receiver', 'content')
    list_filter = ('status',)