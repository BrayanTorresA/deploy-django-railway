from .models import Rent
from .serializer import RentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    # permission_classes = [IsAuthenticated]
