import pytest
from django.test import RequestFactory
from lending import views


@pytest.mark.django_db
class TestViews:
    """Тестирование view-функций приложения lending."""

    @pytest.fixture
    def factory(self):
        return RequestFactory()

    def test_home_view(self, factory):
        """Проверяем, что home view возвращает статус 200."""
        request = factory.get("/")
        response = views.home(request)
        assert response.status_code == 200

    def test_contact_form_view_get(self, factory):
        """Проверяем GET-запрос к contact_form_view."""
        request = factory.get("/send-contact-form/")
        response = views.contact_form_view(request)
        assert response.status_code in [200, 400]

    @pytest.mark.skip
    def test_contact_form_view_post(self, factory):
        """Проверяем POST-запрос к contact_form_view."""
        request = factory.post(
            "/send-contact-form/",
            data={"name": "Test", "email": "test@example.com"},
            content_type="application/x-www-form-urlencoded",
        )
        response = views.contact_form_view(request)
        assert response.status_code == 200
