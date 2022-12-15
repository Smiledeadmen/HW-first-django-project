from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter(original=0, test=0)
counter_click = Counter(original=0, test=0)


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    answ = request.GET['from-landing']
    if answ == 'original':
        counter_click[answ] += 1
        print(counter_click)
        return render(request, 'index.html')
    elif answ == 'test':
        counter_click[answ] += 1
        print(counter_click)
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    answ = request.GET['ab-test-arg']
    if answ == 'original':
        counter_show[answ] += 1
        print(counter_show)
        return render(request, 'landing.html')
    elif answ == 'test':
        counter_show[answ] += 1
        print(counter_show)
        return render(request, 'landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    return render(request, 'stats.html', context={
        'test_conversion': counter_click['test'] / counter_show['test'],
        'original_conversion':counter_click['original'] / counter_show['original'],
    })
