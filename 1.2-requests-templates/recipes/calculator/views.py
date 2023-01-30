import copy

from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def calculate(request, recipes):
    copy_recipe = copy.deepcopy(DATA[recipes])
    context = {'recipe': copy_recipe}
    num = request.GET.get('servings', 1)
    if num != 0:
        for key, value in context['recipe'].items():
            context['recipe'][key] = int(num) * value
        return render(request, 'calculator/index.html', context)
    else:
        return render(request, 'calculator/index.html', context)


def omlet(request):
    return calculate(request, 'omlet')


def pasta(request):
    return calculate(request, 'pasta')


def buter(request):
    return calculate(request, 'buter')
