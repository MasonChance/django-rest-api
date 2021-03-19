from rest_framework import generics
from .serializer import PostSerializer
from .models import Deck
# Create your views here.

class DeckListView(generics.ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = PostSerializer


class DeckDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = PostSerializer