from django.contrib import admin
from .models import UserIncome,Source
# Register your models here.


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('amount','date','description','owner','source')
    search_fields = ('amount','date','description','owner','source')
    list_per_page = 5
    

admin.site.register(UserIncome,ExpensesAdmin)
admin.site.register(Source)

