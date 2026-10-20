"""path("allymailer/", include("allymailer_wrapper.urls")) -> /allymailer/webhook"""
from django.urls import path

from .views import webhook

app_name = "allymailer"
urlpatterns = [path("webhook", webhook, name="webhook")]
