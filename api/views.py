from .serializer import MarriageSerializer, BaptismSerializer,AnnouncementSerializer, ReadingsSerializer
from rest_framework import viewsets, permissions
from .models import Marriage,Baptism, Annoucement,Reading

class MarriageView(viewsets.ModelViewSet):
    queryset = Marriage.objects.all()
    serializer_class = MarriageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BaptismView(viewsets.ModelViewSet):
    queryset = Baptism.objects.all()
    serializer_class = BaptismSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReadingsView(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AnnnoucementView(viewsets.ModelViewSet):
    queryset = Annoucement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
