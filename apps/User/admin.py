from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .Form.form import CustomUserChangeForm, CustomUserCreationForm
from .models import *


# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserAdminCustom(UserAdmin):
    model = User
    search_fields = ('email', 'nickname')
    list_filter = ('email', 'nickname', 'is_active', 'is_staff')
    ordering = ('-created_at',)
    list_display = ('email', 'nickname', 'is_active', 'is_staff')
    fieldsets = (
        ("Important", {'fields': ('email', 'nickname', 'password', 'client')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('phone',)}),
    )
    # formfield_overrides = {
    #     NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    # }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdminCustom)
admin.site.register(Mgmt_portal_user)
admin.site.register(Client, ClientAdmin)
admin.site.register(Image_path)
admin.site.register(Host_user_link)
admin.site.register(User_additional_profile)
