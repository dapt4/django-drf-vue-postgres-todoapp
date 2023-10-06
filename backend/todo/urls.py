from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.get_all_or_create),
    path('todo/<int:id>', views.get_one_edit_delete),
    path('todo/done/<int:id>', views.is_done),
]
