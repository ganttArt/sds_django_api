from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListSinQuote.as_view()),
    path('<int:pk>/', views.DetailSinQuote.as_view()),
]