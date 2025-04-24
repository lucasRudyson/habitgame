from rest_framework.routers import DefaultRouter
from ..views.heroiView import heroiViewSet


heroi_router = DefaultRouter()
heroi_router.register(r'heroi',heroiViewSet,basename='herois')
