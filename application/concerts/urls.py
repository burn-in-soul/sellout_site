from django.urls import include, path
from rest_framework import routers

from application.concerts import views

router = routers.DefaultRouter()
router.register(r'concerts', views.ConcertView)

urlpatterns = [
    path('', include(router.urls)),
]