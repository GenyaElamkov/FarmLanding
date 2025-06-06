from django.urls import path

from . import views

app_name = "lending"

urlpatterns = [
    path("", views.home, name="home"),
    path("send-contact-form/", views.contact_form_view, name="send_contact_form"),
]
