from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Book

# Vista para listar los libros
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

# Vista para crear un nuevo libro
class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'published_date']
    success_url = reverse_lazy('book-list')
