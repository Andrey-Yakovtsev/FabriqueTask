from django.contrib import admin
from .models import Poll, Question, Choise, PollResponse, Answer


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Choise)
class ChoiseAdmin(admin.ModelAdmin):
    pass


class AnswerAdminInline(admin.TabularInline):
    model = Answer
    extra = 1

@admin.register(PollResponse)
class PollResponseAdmin(admin.ModelAdmin):
    # inlines = [AnswerAdminInline]
    pass

