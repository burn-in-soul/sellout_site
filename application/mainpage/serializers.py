from rest_framework import serializers

from application.concerts.models import Concert
from application.mainpage.models import MainpageImages


class MainpageImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainpageImages
        fields = '__all__'
