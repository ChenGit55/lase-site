from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


def create_user_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'sign-up.html', {'form': form})

@login_required
def profile_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'profile.html', {'user': user})
