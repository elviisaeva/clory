from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView

from django.urls import reverse


# def login(request):
#
#     args = {}
#     args.update(csrf(request))
#
#     if request.POST:
#         username = request.POST.get('inputEmail', '')
#         password = request.POST.get('inputPassword', '')
#
#         user = auth.authenticate(username = username, password = password)
#         if user is not None:
#             auth.login(request, user)
#             #return render(request, 'home/')
#             return HttpResponse('Hello user')
#         else:
#             args['login_error'] = 'No matches'
#             return redirect('/')
#     else:
#         return render(request, 'login.html', args)

class SignInFormView(FormView):
    form_class = AuthenticationForm
    # form_class = CustomAuthenticationForm
    template_name = "login.html"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('clorymain:home')


def signup(request):
    return render(request, 'base.html')
