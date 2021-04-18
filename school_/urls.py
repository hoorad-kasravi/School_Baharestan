from django.urls import path

from . import views

urlpatterns = [
    path('create', views.create, name="create.school_"),
    path('read', views.read, name="read.school_"), #localhost:8000/category/read
    path('update/<int:category_id>', views.update, name="update.school_"), #localhost:8000/category/update/id
    path('delete/<int:category_id>', views.delete, name="delete.school_"), #localhost:8000/category/delete/id
]