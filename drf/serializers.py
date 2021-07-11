from django.contrib.auth.models import User
from rest_framework import serializers


from polls.models import Poll, Question, Choise, PollResponse, Answer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'answer_option', 'poll']


class AnswersSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    class Meta:
        model = Answer
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    class Meta:
        model = Poll
        fields = '__all__'


class ChoiseSerializer(serializers.Serializer):
    class Meta:
        model = Choise


class PollResponseSerializer(serializers.Serializer):
    class Meta:
        model = PollResponse
        fields = '__all_'

