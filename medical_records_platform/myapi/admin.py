from django.contrib import admin
from .models import User
from .models import Role
from .models import Measurements
from .models import History
from .models import Billing

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Measurements)
admin.site.register(History)
admin.site.register(Billing)


class RoleInline(admin.TabularInline):
    model = Role

class MeasurementsInline(admin.TabularInline):
    model = Role

class HistoryInline(admin.TabularInline):
    model = Role

class BillingInline(admin.TabularInline):
    model = Role

class UserAdmin(admin.ModelAdmin):
    inlines = [
        RoleInline,
        MeasurementsInline,
        HistoryInline,
        BillingInline
    ]