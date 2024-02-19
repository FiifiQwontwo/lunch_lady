from django.urls import path
from .views import dashboard, student_upboarding, custom_login, student_activate

app_name = 'accounts'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard_url'),
    path('login/', custom_login, name='login_url'),
    path('student/signup/', student_upboarding, name='student_signup_url'),
    path('activate/<uidb64>/<token>/', student_activate, name='student_activate_url'),

]
