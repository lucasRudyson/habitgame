from rest_framework.routers import DefaultRouter
from ..views.historicoHabitoView import HistoricoHabitoViewSet

historico_router = DefaultRouter()
historico_router.register(r'historico',HistoricoHabitoViewSet,basename='historicos')