from django.urls import path
from books import views

urlpatterns = [
    path('',views.BooksList, name='BooksList'),
    path('addbooks/',views.AddBooks, name='AddBooks'),
    path('bookdetail/<int:pk>',views.BookDetail, name='BookDetail'),
    
]
