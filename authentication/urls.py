from .views import RegistrationView,UsernameValdationView, EmailValdationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register',RegistrationView.as_view(),name="register"),
    path('validate-username', csrf_exempt(UsernameValdationView.as_view()),
                                        name="validate-username"),
    path('validate-email',csrf_exempt( EmailValdationView.as_view()), name='validate-email')
                                    
]
