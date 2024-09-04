from django.contrib import admin
from .models import myclass

# Register your models here.
#admin.site.register(myclass)

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("first_nm", "last_nm", "phone", "joined_date",)

admin.site.register(myclass, MemberAdmin)