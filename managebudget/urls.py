from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="managebudget"),
    path('add-managebudget',views.add_managebudget, name="add-managebudget")
]
