from django.urls import path

from .views import (
    programs_view,
    evolution_academy_view,
    evolution_futsal_view,
    private_training_view,
    schools_view,
    lion_cubs_view,
    )

urlpatterns = [
    path('', programs_view, name= 'programs'),
    path('lion-cubs/', lion_cubs_view, name= 'lion-cubs'),
    path('evolution-academy/', evolution_academy_view, name= 'evolution-academy'),
    path('evolution-futsal/', evolution_futsal_view, name= 'evolution-futsal-club'),
    path('private-training/', private_training_view, name= 'private-training'),
    path('schools/', schools_view, name= 'schools'),
]