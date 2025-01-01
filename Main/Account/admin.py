from django.contrib import admin
from Account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'national_code', 'email', 'is_admin')
    list_filter = ('phone_number', 'is_admin')





