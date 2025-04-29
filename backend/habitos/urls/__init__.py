from django.urls import path, include
from .heroi import heroi_router
from .area import area_router
from .habito import habito_router
from .semana import semana_router
from .historicoHabito import historico_router


urlpatterns = [
    path('', include(heroi_router.urls)),
    path('', include(area_router.urls)),
    path('', include(habito_router.urls)),
    path('', include(historico_router.urls)),
    path('', include(semana_router.urls)),

]
