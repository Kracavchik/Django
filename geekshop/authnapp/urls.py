from django.urls import path

import authnapp.views as authnapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authnapp.login, name='login'),
    path('logout/', authnapp.logout, name='logout'),
    path('edit/', authnapp.edit, name='edit'),
    path('register/', authnapp.register, name='register')
]
