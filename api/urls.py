from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('marriage', views.MarriageView)
router.register('baptism', views.BaptismView)
router.register('announcement', views.AnnnoucementView)
router.register('readings', views.ReadingsView)
urlpatterns = [
   path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
   path('', include(router.urls))
]
