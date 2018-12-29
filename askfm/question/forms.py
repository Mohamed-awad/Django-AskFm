from django import forms
from .models import Question


class QuestionCreateForm(forms.ModelForm):

  class Meta:
    model = Question
    fields = ['body', 'answer', 'status']

  def __init__(self, *args, **kwargs):
    super(QuestionCreateForm, self).__init__(*args, **kwargs)
    self.fields['body'].label = 'Question'
    self.fields['body'].widget.attrs['readonly'] = True
    self.fields['body'].widget.attrs['rows'] = '1'