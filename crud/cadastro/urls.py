from django.urls import path
from . import views

urlpatterns = [
    path('listPessoa', views.listPessoa,name='list-pessoa'),
    path('',views.createPessoa,name='create-pessoa'),
    path('updatePessoa/<int:id>',views.updatePessoa,name='update-pessoa'),
    path('deletePessoa/<int:id>',views.deletePessoa,name='delete-pessoa')
]