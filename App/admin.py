

# Register your models here.
from django.contrib import admin
from .models import UserProfile, UserActivity

# admin.site.register(UserProfile)
# admin.site.register(UserActivity)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'signup_date')  # Fields to display in the admin list view
    search_fields = ('username', 'email')  # Fields to search in the admin interface
    ordering = ('signup_date',)  # Default ordering by signup date

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity', 'timestamp')  # Fields to display in the admin list view
    search_fields = ('user__username', 'activity')  # Enable searching by username and activity
    list_filter = ('timestamp',)  # Add filtering options by timestamp
    ordering = ('-timestamp',)  # Default ordering by timestamp, newest first