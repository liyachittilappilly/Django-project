from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Save user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Create profile for the new user
            Profile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                phone=form.cleaned_data['phone'],
                college=form.cleaned_data['college'],
                degree=form.cleaned_data['degree'],
                branch=form.cleaned_data['branch'],
            )

            # Redirect to login page after successful registration
            return redirect('/accounts/login/')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard(request):
    # Get profile if exists, otherwise create it safely
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={
            'full_name': request.user.username,
            'phone': '',
            'college': '',
            'degree': '',
            'branch': '',
        }
    )

    return render(request, 'accounts/dashboard.html', {
        'name': profile.full_name
    })
