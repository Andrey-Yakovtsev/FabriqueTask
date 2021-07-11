from django.urls import path, include
from rest_framework import routers

from drf.views import PollViewSet, UserViewSet, QuestionViewSet, ActivePollViewSet, PollResponseViewSet, AnswersViewSet, \
    UserPollsViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register('polls', PollViewSet, basename='polls')
router.register('activepolls', ActivePollViewSet, basename='activepolls')
router.register('questions', QuestionViewSet, basename='questions')
router.register('users', UserViewSet, basename='users')
router.register('answers', AnswersViewSet, basename='answers')
router.register('pollresponse', PollResponseViewSet, basename='pollresponse')
router.register('userpolls', UserPollsViewSet, basename='userpolls')

urlpatterns = [
    path('', include(router.urls)),
]
