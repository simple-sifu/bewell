from rest_framework import routers

from .views import FacilitiesViewSet

router = routers.SimpleRouter()

router.register(r'facilities', FacilitiesViewSet,
                basename="facility")

urlpatterns = router.urls


facilities_list = FacilitiesViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
facilities_detail = FacilitiesViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})