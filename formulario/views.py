from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
 

def register(request):
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           with transaction.atomic():
               user = form.save()
               try:
                    group = Group.objects.get(name='Operarios')
                    user.groups.add(group)
               except ObjectDoesNotExist:
                   messages.warning(request, 'El grupo no existe')
               return redirect('home')
       else:
           messages.error('corriga los errores de formulario')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
                   

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        messages.success(self.request, 'Inicio de sesión exitoso, Bienvenido(a)!')
        return reverse_lazy('formulario:home')
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
def home(request):
    return render(request, 'accounts/home.html')