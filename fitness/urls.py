from django.conf.urls import url, include
from rest_framework_mongoengine.routers import DefaultRouter
from api import FeedViewSet
from fitness.api import FeedListView, UserCreateView

router = DefaultRouter()
router.register(r'feeds', FeedViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^feed_list$', FeedListView.as_view()),
    url(r'^create_user$', UserCreateView.as_view()),
]