from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """register new users"""
    if request.method != 'POST':
        """display blank registration"""
        form = UserCreationForm()
    else:
        """process completed form"""
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    # render blank or invalid form
    context = {'Form': form}
    return render(request, 'registration/register.xhtml', context)


