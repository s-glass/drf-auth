from rest_framework import generics
from .serializer import TacoSerializer
from .models import Taco
from .permissions import IsOwnerOrReadOnly


class TacoList(generics.ListCreateAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Taco.objects.all()
    serializer_class = TacoSerializer


class TacoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Taco.objects.all()
    serializer_class = TacoSerializer