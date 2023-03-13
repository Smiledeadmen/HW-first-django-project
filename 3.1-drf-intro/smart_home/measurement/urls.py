from django.urls import path
from django.contrib import admin

from .views import SensorView, MeasurementView, SensorIdView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorIdView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
