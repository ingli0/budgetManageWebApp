from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="managebudget"),
    path('add-managebudget',views.add_managebudget, name="add-managebudget"),
    path('edit-expense/<int:id>',views.expense_edit, name="edit-expense"),
    path('expense-delete/<int:id>',views.delete_expense, name="expense-delete"),
    path('search-expenses',csrf_exempt(views.search_expenses), name="search_expenses"),
    path('expense_category_summary',views.expense_category_summary,name='expense_category_summary'),
    path('stats',views.statsView,name='stats'),
    path('export_csv',views.export_csv,name='export-csv'),
    path('export_excel',views.export_excel,name='export-excel')
]
 