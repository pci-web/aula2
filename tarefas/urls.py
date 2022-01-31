from django.urls import path
from tarefas import views


urlpatterns = [
    path('', views.index_view, name="index"),
    path('form/', views.form_view, name="form"),
    path('apagar/<int:tarefa_id>', views.apagar_view, name="apagar")
]