from django.urls import path

from . import views

from .views import MainView, DetailView, CreateView, OSDeleteView, index
urlpatterns = [
#    path('', index, name='index'),
    path('', MainView.as_view(), name='main'),
    path('detail/<int:pk>',DetailView.as_view(), name='detail'),
    path('create',CreateView.as_view(), name='create'),
    path('delete/<int:pk>',OSDeleteView.as_view(), name='delete'),
]
