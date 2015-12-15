from django.contrib import admin
from homepage.models import User


admin.site.register(User)



# from django.contrib import admin
# from homepage.models import User

# from django.contrib.auth.admin import UserAdmin

# from django.contrib.auth import get_user_model
# User = get_user_model()


# class CustomUserAdmin(UserAdmin):
#     # as an example, this custom user admin orders users by email address
#     # ordering = ('email',)
#     model = User
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
#         (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
#         (('Important dates'), {'fields': ('last_login', 'date_joined')}),
#         (('Groups'), {'fields': ('groups',)}),
#         (('Files'), {'fields': ('avatar',)}),
#     )


# # admin.site.register(User)


# # admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)