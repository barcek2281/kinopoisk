from re import L
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from users.forms import UserCreationForm, UserProfileForm


# Create your views here.
class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }

        return render(request, self.template_name, context)

    def post(self, request):

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

        context ={
            'form': form
        }
        return render(request, self.template_name, context)
    
@login_required
def profile_page(request):
	user = request.user
    
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = UserProfileForm(instance=user)
                  
	return render(request, 'users/profile.html', {'form': form})