from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request,f'Welcome {username}, your account is created')
      return redirect('login')
  else:
    form = RegistrationForm()
  return render (request, 'users/register.html', {'form':form})

# Display error message when logged out
@login_required
def profile_page(request):
  return render(request, 'users/profile.html')