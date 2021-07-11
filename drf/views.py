import datetime

from django.contrib.auth.models import User
from rest_framework import viewsets, request
from rest_framework.request import Request

from polls.models import Poll, Question, PollResponse, Answer
from .serializers import UserSerializer, PollSerializer, QuestionSerializer, \
    PollResponseSerializer, AnswersSerializer  # , ActivePollSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Сериалайзер для пользователей
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PollViewSet(viewsets.ModelViewSet):
    """
    Сериалайзер для опросов
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ActivePollViewSet(viewsets.ModelViewSet):
    """
    Сериалайзер для активных опросов
    """
    queryset = Poll.objects.exclude(
        # enddate__lt=datetime.datetime.now(),
        startdate__gt=datetime.datetime.now()
    )
    serializer_class = PollSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    Сериалайзер для вопросов
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswersViewSet(viewsets.ModelViewSet):
    """
    Сериалайзер для ответов
    """
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer


class PollResponseViewSet(viewsets.ModelViewSet):
    """
    Сериалайзер для заполненных опросов
    """
    queryset = PollResponse.objects.all()
    serializer_class = PollResponseSerializer


class UserPollsViewSet(viewsets.ModelViewSet):
    '''
    Опросы пройденные пользователем
    '''
    # user_id = Request.user.id
    queryset = PollResponse.objects.filter(user=1) #TODO поправить выборку
    serializer_class = PollResponseSerializer

