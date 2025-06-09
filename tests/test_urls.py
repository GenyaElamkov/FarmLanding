import pytest
from django.urls import reverse, resolve
from lending import views


class TestUrls:
    def test_home_url(self) -> None:
        url = reverse("lending:home")
        assert url == "/"

        resolved = resolve("/")
        assert resolved.func == views.home
        assert resolved.app_name == "lending"
        assert resolved.url_name == "home"

    def test_send_contact_form(self) -> None:
        url = reverse("lending:send_contact_form")
        assert url == "/send-contact-form/"

        resolved = resolve("/send-contact-form/")
        assert resolved.func == views.contact_form_view
        assert resolved.app_name == "lending"
        assert resolved.url_name == "send_contact_form"
