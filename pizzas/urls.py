from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Strona główna
    path('', views.index, name='index'),
    # Wyświetlenie wszystkich pizz
    path('pizzs/', views.pizzs, name='pizzs'),
    # API endpoints dla pizz
    path('pizzas_api/', views.PizzaList.as_view()),
    path('pizzas_api/<int:pk>', views.PizzaDetail.as_view()),
]
