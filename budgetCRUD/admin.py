from django.contrib import admin
from .models import user,transaction,budget

# Register your models here.
admin.site.register(user)
admin.site.register(transaction)
admin.site.register(budget)