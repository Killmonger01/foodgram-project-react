from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()

NAME_MAX_LENGTH = 300
COLOR_MAX_LENGTH = 7
MEASUREMENT_UNIT_MAX_LENGTH = 50


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=NAME_MAX_LENGTH,)
    measurement_unit = models.CharField(
        verbose_name='Измерение',
        max_length=MEASUREMENT_UNIT_MAX_LENGTH)


class Tag(models.Model):
    name = models.CharField(
        verbose_name="Тэг",
        max_length=NAME_MAX_LENGTH,
        unique=True)
    color = models.CharField(
        verbose_name="Цвет",
        max_length=COLOR_MAX_LENGTH,
        unique=True)
    slug = models.SlugField(
        verbose_name="Слаг",
        unique=True)


class Recipe(models.Model):
    TEXT_MAX_LENGTH = 250
    name = models.CharField(
        verbose_name="Название",
        max_length=NAME_MAX_LENGTH
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        related_name="recipes",
        on_delete=models.SET_NULL,
        null=True)
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="recipe_images/",
    )
    text = models.TextField(
        verbose_name="Описание блюда",
        max_length=TEXT_MAX_LENGTH,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name="Ингредиенты",
        related_name="recipes",)
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Тег",
        related_name="recipes",)
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        validators=[MinValueValidator(1, message='Минимальное значение 1!')]
    )


class IngredientInRecipe(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient_list',
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    amount = models.PositiveSmallIntegerField(
        'Количество',
        validators=[MinValueValidator(1, message='Минимальное количество 1!')]
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецептах'


class Favourite(models.Model):
    """ Модель Избранное """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique_favourite')
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Избранное'


class ShoppingCart(models.Model):
    """ Модель Корзина покупок """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'Корзина покупок'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique_shopping_cart')
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Корзину покупок'
