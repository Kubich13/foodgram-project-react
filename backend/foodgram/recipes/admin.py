from django.contrib import admin

from . import models


class RecipeIngredientInline(admin.TabularInline):
    model = models.Recipe.ingredients.through
    min_num = 1
    extra = 0


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'measurement_unit')
    list_filter = ('name', )
    search_fields = ('name', )


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'color', 'slug')
    list_editable = ('name', 'color', 'slug')
    empty_value_display = '-пусто-'


@admin.register(models.RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'recipe', 'ingredient', 'amount')
    list_editable = ('recipe', 'ingredient', 'amount')


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author', 'in_favorites',
                    'cooking_time', 'text', 'image')
    list_editable = (
        'name', 'cooking_time', 'text',
        'image', 'author'
    )
    readonly_fields = ('in_favorites',)
    empty_value_display = '-пусто-'
    search_fields = ('name', 'author', 'tags')
    list_filter = ('name', 'author', 'tags')
    inlines = (RecipeIngredientInline,)

    @admin.display(description='Избранное')
    def in_favorites(self, obj):
        return obj.favorite_recipe.count()


@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')
    list_editable = ('user', 'recipe')


@admin.register(models.ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')
    list_editable = ('user', 'recipe')
