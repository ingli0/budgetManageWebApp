from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="managebudget"),
    path('add-managebudget',views.add_managebudget, name="add-managebudget"),
    path('edit-expense/<int:id>',views.expense_edit, name="edit-expense"),
    path('expense-delete/<int:id>',views.delete_expense, name="expense-delete")
]
