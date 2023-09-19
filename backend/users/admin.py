from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import display

from .models import Subscribe, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'id',
        'email',
        'first_name',
        'last_name',
        'sub_count',
        'recipe_count',
    )
    readonly_fields = ('sub_count', 'recipe_count')
    list_filter = ('email', 'first_name')

    @display(description='Количество в подписчиков')
    def sub_count(self, obj):
        return obj.subscriber1.count()

    @display(description='Количество рецептов')
    def recipe_count(self, obj):
        return obj.recipes.count()


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'author',)
