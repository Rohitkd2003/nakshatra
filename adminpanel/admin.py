from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from community.models import Post as CommunityPost, Comment as CommunityComment

def _safe_unregister(model):
    try:
        admin.site.unregister(model)
    except NotRegistered:
        pass

# Hide selected models from admin
for _model in (Group, Token, CommunityPost, CommunityComment):
    _safe_unregister(_model)

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')


from django.contrib import admin
from .models import Post, Comment, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at', 'updated_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'content', 'created_at')
    search_fields = ('content', 'user__username', 'post__title')
    list_filter = ('created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at')
    search_fields = ('user__username', 'post__title')
    list_filter = ('created_at',)


from django.contrib import admin
from nutrition.models import MealPlan, FoodItem

@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at',)

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'calories', 'protein', 'carbs', 'fats')
    search_fields = ('name',)


from django.contrib import admin
from resources.models import Resource
from payments.models import Payment
from notifications.models import Notification

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'created_at')
    search_fields = ('title',)
    list_filter = ('type', 'created_at')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'status', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('status', 'created_at')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'read', 'created_at')
    search_fields = ('message', 'user__username')
    list_filter = ('read', 'created_at')
