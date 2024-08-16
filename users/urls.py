from django.urls import path
from .views import registerUser

urlpatterns = [
    path('registrar/', registerUser, name= 'registrarUsuario'),
]