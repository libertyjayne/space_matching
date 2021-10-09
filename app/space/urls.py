from django.urls import path, include
from rest_framework.routers import DefaultRouter

from space import views


router = DefaultRouter()
router.register('spaces', views.SpaceViewSet)

app_name = 'space'

urlpatterns = [
    path('', include(router.urls))
]
