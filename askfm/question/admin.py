from django.contrib import admin
from .models import Question, Like


class QuestionAdmin(admin.ModelAdmin):
  list_display = ('id', 'sender', 'receiver', 'status', 'created',)
  list_filter = ('created', 'publish', 'sender', 'receiver', 'status')
  search_fields = ('sender', 'receiver')
  date_hierarchy = 'publish'
  ordering = ['status', 'publish']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Like)
