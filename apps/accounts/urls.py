from django.urls import path


from .views import (
    profile_view,
    create_user_view,
)

urlpatterns = [
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('sign-up/', create_user_view, name='sign-up'),
]