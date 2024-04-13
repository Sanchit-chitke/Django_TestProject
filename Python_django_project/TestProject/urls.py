from django.urls import path
from .views import create_first_entry,create_second_entry,create_third_entry, show_third_entry

urlpatterns = [
    path('', create_first_entry, name='create_first_entry'),
    path('second/', create_second_entry, name='create_second_entry'),
    path('third/', create_third_entry, name='create_third_entry'),
    path('show/', show_third_entry, name='show_third_entry'),
]
