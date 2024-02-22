
from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name="preferences"),
    path('general',views.general,name="general")
]