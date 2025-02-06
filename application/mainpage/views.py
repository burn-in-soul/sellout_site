from rest_framework.viewsets import ReadOnlyModelViewSet

from application.mainpage.models import MainpageImages
from application.mainpage.serializers import MainpageImagesSerializer


class MainpageImagesView(ReadOnlyModelViewSet):
    queryset = MainpageImages.objects.all()
    serializer_class = MainpageImagesSerializer
