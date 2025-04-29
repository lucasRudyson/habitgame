from rest_framework.routers import DefaultRouter
from ..views.areaView import AreaViewSet
area_router = DefaultRouter()
area_router.register(r'area',AreaViewSet,basename='areas')