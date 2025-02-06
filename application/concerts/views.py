from rest_framework.viewsets import ReadOnlyModelViewSet

from application.concerts.models import Concert
from application.concerts.serializers import ConcertSerializer


class ConcertView(ReadOnlyModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer