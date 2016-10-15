import json
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from fitness.models import Feed, Question, Option, User

class FeedListView(View):
    def post(self, *args, **kwargs):
        return HttpResponse(Feed.objects.all().to_json(), content_type='application/json')

class UserCreateView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        user_dict = json.loads(self.request.body)
        user = User(**user_dict)
        user.clean()
        user.save()
        return HttpResponse(user.to_json(), content_type='application/json')
