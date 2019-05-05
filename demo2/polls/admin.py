from django.contrib import admin
from.models import Question,Choice
# Register your models here.
class ChoiceInlines(admin.StackedInline):
    model =Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['desctext',]
    inlines = [ChoiceInlines,]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)