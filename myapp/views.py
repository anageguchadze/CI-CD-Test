from rest_framework import viewsets
from .models import *
from .serializers import *


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
