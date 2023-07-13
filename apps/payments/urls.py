from django.urls import path
from .views import (
    subscription_view,
    payment_view,
    successfully_enrolled_view,
)

urlpatterns = [
    path('', payment_view, name='payment'),
    path('subscription/', subscription_view, name='subscription'),
    path('successfully-enrolled/', successfully_enrolled_view, name="successfully enrolled"),
]