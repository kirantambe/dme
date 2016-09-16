from django.conf.urls import url, include
from rest_framework_mongoengine.routers import DefaultRouter
from api import FeedViewSet

router = DefaultRouter()
router.register(r'feeds', FeedViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]