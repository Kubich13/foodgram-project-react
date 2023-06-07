from django.http import HttpResponse


def make_list_ingredients(self, request, ingredients):
    shopping_list = ['Список покупок:\n']
    for ingredient in ingredients:
        name = ingredient['ingredient__name']
        unit = ingredient['ingredient__measurement_unit']
        amount = ingredient['ingredient_amount']
        shopping_list.append(f'\n{name} - {amount}, {unit}')
    response = HttpResponse(shopping_list, content_type='text/plain')
    response['Content-Disposition'] = (
        'attachment; filename="shopping_cart.txt"')
    return response
