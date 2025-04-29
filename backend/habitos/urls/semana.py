from rest_framework.routers import DefaultRouter
from ..views.semanaView import SemanaViewSet

semana_router = DefaultRouter()
semana_router.register(r'semana',SemanaViewSet,basename='semanas')