from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Book
from .serializers import Bookserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Bookserializer


# Create your views here.

@api_view(['GET'])
def BooksList(request):
    
    books=Book.objects.all()
    serializer=Bookserializer(books,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def AddBooks(request):
    serializer=Bookserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def BookDetail(request,pk):
    try:
       books= Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=Bookserializer(books)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=Bookserializer(books,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        books.delete()
