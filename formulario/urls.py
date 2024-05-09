from django.urls import path
from .views import register, home, CustomLoginView, CustomLogoutView
#* http://127.0.0.1:8000/accounts/register
#* http://127.0.0.1:8000/accounts/home
#* http://127.0.0.1:8000/accounts/logout
urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home' ),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout" ),
    # path('home/'),
]
