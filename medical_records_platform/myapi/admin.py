from django.contrib import admin
from .models import User
from .models import Role

# Register your models here.
admin.site.register(User)
admin.site.register(Role)


class RoleInline(admin.TabularInline):
    model = Role

class UserAdmin(admin.ModelAdmin):
    inlines = [
        RoleInline,
    ]