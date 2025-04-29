from rest_framework.routers import DefaultRouter
from ..views.habitoView import HabitoViewSet

habito_router = DefaultRouter()
habito_router.register(r'habito',HabitoViewSet,basename='habitos')
