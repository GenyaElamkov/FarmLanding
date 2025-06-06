from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from .service.telegram_utils import send_telegram_message


def home(request):
    return render(request, "base.html")


def contact_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        # Формируем сообщение для Telegram
        telegram_msg = (
            f"<b>Новое сообщение с сайта</b>\n\n"
            f"<b>Имя:</b> {name}\n"
            f"<b>Email:</b> {email}\n"
            f"<b>Телефон:</b> {phone}\n"
            f"<b>Сообщение:</b>\n{message}"
        )

        # Отправляем в Telegram
        bot_token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID

        if send_telegram_message(bot_token, chat_id, telegram_msg):
            return JsonResponse({'status': 'success', 'message': 'Сообщение отправлено!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Ошибка при отправке сообщения'}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Неверный метод запроса'}, status=400)