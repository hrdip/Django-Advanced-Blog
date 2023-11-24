from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django import forms
# Register your models here.

# class CustomUserCreationsForm(UserCreationForm):
#     '''
#       for add our custom form
#     '''
#     class Meta:
#         model = User
#         fields = ('email',)

# class CustomUserChangesForm(UserCreationForm):
#     '''
#       for change our custom form
#     '''
#     password1 = forms.CharField(label='password1',widget=forms.PasswordInput)       
#     password1 = forms.CharField(label='password1',widget=forms.PasswordInput) 
#     ''' for custom form most use minimum required from base model'''



class CustomUserAdmin(UserAdmin):
    model = User
    # add_form = CustomUserCreationsForm
    # change_password_form = CustomUserChangePasswordForm
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    searching_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentication', {
            "fields": (
                'email','password'
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff','is_superuser','is_active'
                ),
        }),
         ('Group permissions', {
            "fields": (
                'groups','user_permissions'
                ),
        }),
         ('Important date', {
            "fields": (
                'last_login',
                ),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email','password1','password2','is_staff','is_active','is_superuser'
                ),
        }),
    )



    
admin.site.register(Profile)
admin.site.register(User,CustomUserAdmin)