from django.contrib import admin
from . models import MensData,WomensData,KidsData,LoginData,OrdersData

# Register your models here.

class MensDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(MensData, MensDataAdmin)

class WomensDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(WomensData, WomensDataAdmin)

class KidsDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(KidsData, KidsDataAdmin)

class LoginDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(LoginData, LoginDataAdmin)

class OrdersDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(OrdersData, OrdersDataAdmin)