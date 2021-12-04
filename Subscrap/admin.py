from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as useradmin
from .models import *

class UserAdmin(useradmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(students, UserAdmin)

admin.site.register(sublist)

admin.site.register(prebuildsublist)