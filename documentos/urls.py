from django.urls import path
from .views import responder_pergunta

urlpatterns = [
    path('responder/', responder_pergunta, name='responder_pergunta'),
]
