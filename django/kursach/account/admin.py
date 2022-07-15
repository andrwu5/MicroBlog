from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    search_fields = ('email', 'username', )
    readonly_fields = ('date_joined', 'last_login')
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    
    list_filter = ()
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

