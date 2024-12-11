import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WhatsAppMessage

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = WhatsAppMessage.objects.create(
                sender=data.get('sender'),
                receiver=data.get('receiver'),
                content=data.get('content'),
                status='received',
            )
            return JsonResponse({'status': 'success', 'message_id': message.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=405)

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = WhatsAppMessage.objects.create(
                sender=data.get('sender'),
                receiver=data.get('receiver'),
                content=data.get('content'),
                status='sent',
            )
            return JsonResponse({'status': 'success', 'message_id': message.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=405)