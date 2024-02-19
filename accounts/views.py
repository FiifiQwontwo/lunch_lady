from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages, auth
from django.contrib.auth import get_user_model, login, authenticate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')


def get_user_agents(request):
    return request.META.get('HTTP_USER_AGENT', '')


def student_activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        User = get_user_model()
        user = User._default_manager.get(slug=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request,'User Accounts Activated Successfully')
        return redirect('accounts: dashboard_url')
    else:
        messages.error(request,'Invalid Activation Link')
        return redirect('account:dashboard_url')


def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                messages.success(request,'Login Successfully')
                user_agent = get_user_agents(request)
                request.session['is_mobile'] = 'Mobile' in user_agent

                if user.is_student:
                    return redirect('accounts:dashboard_url') # I have to change this to student profile

                elif user.is_lecturer:
                    return redirect('accounts:dashboard_url') # I have to change to lecture profile
                elif user.is_staff:
                    return redirect('accounts:dashboard_url') #
            else:
                messages.error(request,'Your account is not active. Please activate your account')
        else:
            messages.error(request,'Loin credentials Not valid. Please!!')
    return render(request, 'students/login.html')


