from django.shortcuts import render
from .models import Pizza
from .serializers import PizzaSerializer
from rest_framework import generics, permissions


def index(request):
    return render(request, 'pizzas/index.html')


def pizzs(request):
    """Wyświetlenie wszystkich pizz"""
    pizzs = Pizza.objects.order_by('date_added')
    context = {'pizzs': pizzs}
    return render(request, 'pizzas/pizzs.html', context)


class PizzaList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PizzaSerializer


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PizzaSerializer


