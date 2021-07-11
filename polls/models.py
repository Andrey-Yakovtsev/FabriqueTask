from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    '''
    Модель опросника
    '''
    title = models.CharField(blank=False, max_length=300)
    startdate = models.DateTimeField(blank=False)
    enddate = models.DateTimeField(blank=False)
    description = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    '''
    Модель вопроса к опроснику. Связь с опросником через ID
    '''
    QUESTION_CHOICES = (
        (u'1', u'Text'),
        (u'2', u'Radio'),
        (u'3', u'Checkbox'),
    )
    answer_option = models.CharField(max_length=1, choices=QUESTION_CHOICES)
    poll = models.ManyToManyField(Poll)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text


class Answer(models.Model):
    '''
    Модель ответов
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    free_answer = models.CharField(max_length=50, help_text='max 50 simbols', default='', blank=True, null=True)
    variant1 = models.CharField(max_length=50, help_text='max 50 simbols', default='', blank=True, null=True)
    variant2 = models.CharField(max_length=50, help_text='max 50 simbols', default='', blank=True, null=True)
    variant3 = models.CharField(max_length=50, help_text='max 50 simbols', default='', blank=True, null=True)

    def __str__(self):
        return self.question.text

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)

    def __str__(self):
        return self.choice_text


class PollResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(null=True, blank=True, default='', max_length=50)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
