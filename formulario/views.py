from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.
# TODO: crear funcionalidad de poder registrarse y el login internamente dentro de este metodo
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            # Asignar al usuario a un group
            group = Group.objects.get(name='Operarios')
            user.groups.add(group)
            messages.success(request, 'Registro exitoso. Bienvenido!')
            return redirect('home')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += 'is-invalid'
            messages.error(request, 'Por favor corrija los errores en el formulario')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        messages.success(self.request, 'Inicio de sesión exitoso, Bienvenido(a)!')
        return reverse_lazy('home')
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
@login_required
def home(request):
    return render(request, 'accounts/home.html')
    