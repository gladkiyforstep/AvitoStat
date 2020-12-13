from django.urls import path
from .views import AddView, StatView

app_name = "AvitoStat"

urlpatterns = [
    path('add/', AddView.as_view()),
    path('stat/', StatView.as_view()),
]
