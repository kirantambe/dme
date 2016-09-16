from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from rest_framework_mongoengine.viewsets import ModelViewSet

from contacts.models import Feed, Question, Option


class OptionSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Option


class QuestionSerializer(EmbeddedDocumentSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question


class FeedSerializer(DocumentSerializer):
    questions = QuestionSerializer(many=True)

    def create(self, validated_data):
        questions = validated_data.pop('questions')
        return Feed.objects.create(questions=questions, **validated_data)

    class Meta:
        model = Feed


class FeedViewSet(ModelViewSet):
    serializer_class = FeedSerializer
    queryset = Feed.objects.all()