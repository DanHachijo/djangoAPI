from tickets.views import TicketViewSet, CategoryViewSet
from members.views import MemberViewSet
from customers.views import StoreViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('staff', MemberViewSet)
router.register('store', StoreViewSet)
router.register('ticket-categories', CategoryViewSet)
router.register('tickets', TicketViewSet)
# urlpatterns = router.urls
