from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from .forms import FeedbackForm
from .service.telegram_utils import send_telegram_message


def home(request):
    form = FeedbackForm()  # Создаем пустую форму
    return render(request, "base.html", {'form': form})


def contact_form_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

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
                return JsonResponse(
                    {
                        'status': 'success',
                        'message': 'Сообщение отправлено!',
                    },
                )
            else:
                return JsonResponse(
                    {
                        'status': 'error',
                        'message': 'Ошибка при отправке сообщения',
                    }, status=500,
                )
        else:
            # Если форма не валидна, возвращаем ошибки
            return JsonResponse(
                {
                    'status': 'error',
                    'message': 'Пожалуйста, проверьте правильность заполнения формы',
                }, status=400,
            )

    return JsonResponse(
        {
            'status': 'error',
            'message': 'Неверный метод запроса',
        }, status=400,
    )
