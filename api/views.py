from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Book

# Vista para listar los libros
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

# Vista para crear un nuevo libro
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'published_date']
    success_url = reverse_lazy('book-list')
    login_url = reverse_lazy('login')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book-list') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})