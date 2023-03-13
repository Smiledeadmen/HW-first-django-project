# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        new_sensor = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description']
        )
        return Response({'post': SensorDetailSerializer(new_sensor).data})


class SensorIdView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer



class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        sensor = Sensor.objects.get(pk=request.data['sensor'])
        new_temp = Measurement.objects.create(
            sensor=sensor,
            temperature=request.data['temperature']
        )
        return Response({'post': MeasurementSerializer(new_temp).data})