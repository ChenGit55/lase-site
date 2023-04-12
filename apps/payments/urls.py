from django.urls import path
from .views import (
    subscription_view,
    payment_view,
)

urlpatterns = [
    path('', payment_view, name='payment'),
    path('subscription/', subscription_view, name='subscription')
]