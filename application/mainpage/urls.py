from django.urls import include, path
from rest_framework import routers

from application.mainpage import views

router = routers.DefaultRouter()
router.register(r'images', views.MainpageImagesView)

urlpatterns = [
    path('', include(router.urls)),
]