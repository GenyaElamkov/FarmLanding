from django import forms

from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ваше имя"}
        ),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Ваш email"}
        ),
    )

    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ваш телефон"}
        ),
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"class": "form-control", "rows": 4, "placeholder": "Ваше сообщение"}
        ),
    )
