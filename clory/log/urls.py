from django.urls import path
from . import views

urlpatterns = [
    path('signIn/', views.SignInFormView.as_view(), name = 'sign_in'),
    path('signup/', views.signup, name = 'signup'),

]
