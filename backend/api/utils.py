from datetime import datetime

from django.db.models import Sum

from recipes.models import IngredientInRecipe


def generate_shopping_list(user):
    if not user.shopping_cart.exists():
        return None

    ingredients = IngredientInRecipe.objects.filter(
        recipe__shopping_cart__user=user
    ).values(
        'ingredient__name',
        'ingredient__measurement_unit'
    ).annotate(amount=Sum('amount'))

    today = datetime.today()
    shopping_list = (
        f'Shopping list for: {user.get_full_name()}\n\n'
        f'Date: {today:%Y-%m-%d}\n\n'
    )
    shopping_list += '\n'.join([
        f'- {ingredient["ingredient__name"]} '
        f'({ingredient["ingredient__measurement_unit"]})'
        f' - {ingredient["amount"]}'
        for ingredient in ingredients
    ])
    shopping_list += f'\n\nFoodgram ({today:%Y})'

    return shopping_list
