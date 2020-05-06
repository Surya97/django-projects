from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class ChoiceAdmin(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceAdmin]


admin.site.register(Question, QuestionAdmin)
