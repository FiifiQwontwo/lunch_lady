from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.contrib.auth.models import AnonymousUser
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')


def get_user_agents(request):
    return request.META.get('HTTP_USER_AGENT', '')