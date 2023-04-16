from django.urls import path


from .views import (
    login_view,
    logout_view,
    profile_view,
    create_user_view,
    edit_profile_view,
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('sign-up/', create_user_view, name='sign-up'),
    path('edit-profile/<int:user_id>/', edit_profile_view, name='edit-profile')
]