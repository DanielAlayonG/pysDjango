from django.urls import path
from .views import BookListView, BookCreateView, login_view

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/new/', BookCreateView.as_view(), name='book-create'),
    path('login/', login_view, name='login'),  # Ruta para la vista de login
]
