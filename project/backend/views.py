# Create your views here.
from rest_framework import generics

from .models import Book
from .serializers import BookSerializers


class CreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def perform_create(self, serializer):
        serializer.save()
