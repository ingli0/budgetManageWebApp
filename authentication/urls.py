from .views import RegistrationView,UsernameValdationView, EmailValdationView,VerificationView,LoginView,LogoutView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register',RegistrationView.as_view(),name="register"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('validate-username', csrf_exempt(UsernameValdationView.as_view()),
                                        name="validate-username"),
    path('validate-email',csrf_exempt( EmailValdationView.as_view()), name='validate-email'),
    path('activate/<uidb64>/<token>',VerificationView.as_view(),name='activate')
                                    
]
