from django.shortcuts import render
from .models import Book
from .converters import DateConverter
def books_view(request):
    template = 'books/books_list.html'
    books_obj = Book.objects.all()
    context = {'books': books_obj}
    return render(request, template, context)

def book_details(request, pub_date):
    template = 'books/book_details.html'
    converter = DateConverter()
    prev_date_book = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').values('pub_date').last()
    next_date_book = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').values('pub_date').first()
    if prev_date_book is not None:
        prev_date_book = converter.to_url(prev_date_book['pub_date'])
    if next_date_book is not None:
        next_date_book = converter.to_url(next_date_book['pub_date'])

    book = Book.objects.get(pub_date=pub_date)
    context = {'book': book,
               'prev_date_book': prev_date_book,
               'next_date_book': next_date_book,
               }
    return render(request, template, context)