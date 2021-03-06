# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics

from .models import Book
from .serializers import BookSerializers


def home(request):
    # boards = Board.objects.all()
    return render(request, 'home.html')

def index(request):
    return HttpResponse("Hello, world. I am creating the hamro pustak bhandar.")


class CreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def perform_create(self, serializer):
        serializer.save()
