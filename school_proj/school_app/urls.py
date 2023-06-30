from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('signout/', views.signout, name='signout'),
    path('form/', views.form_view, name='form_view'),
]



