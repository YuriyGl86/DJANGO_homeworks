from django.shortcuts import render, redirect

from books.models import Book


def books_view(request):
    return redirect('books_list', permanent=True)


def books_list(request):
    template = 'books/books_list.html'
    books_list = Book.objects.all()
    context = {'books': books_list}
    return render(request, template, context)


def books_list_for_date(request, dt):
    book_list = Book.objects.filter(pub_date=dt)
    try:
        prev_obj = book_list[0].get_previous_by_pub_date()
    except:
        prev_obj = None
    try:
        next_obj = book_list[0].get_next_by_pub_date()
    except:
        next_obj = None
    context = {'books': book_list,
               'prev_obj': prev_obj,
               'next_obj': next_obj}
    template = 'books/books_list_date.html'
    return render(request, template, context)
