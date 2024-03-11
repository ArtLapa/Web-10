from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page or any other page
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})
