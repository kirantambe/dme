from django.conf.urls import url
from fitness.api import FeedListView, UserCreateView


urlpatterns = [
    url(r'^feed_list$', FeedListView.as_view()),
    url(r'^create_user$', UserCreateView.as_view()),
]