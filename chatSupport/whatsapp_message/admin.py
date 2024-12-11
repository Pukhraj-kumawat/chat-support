from django.contrib import admin
from .models import WhatsAppMessage

admin.site.register(WhatsAppMessage)

# @admin.register(WhatsAppMessage)
# class WhatsAppMessageAdmin(admin.ModelAdmin):
#     list_display = ('sender', 'timestamp', 'status')
#     search_fields = ('sender','content')
#     list_filter = ('status',)