
from django import forms
from chatbotFAQ.models import Question

class QuestionForm(forms.ModelForm):
   class Meta:
     model = Question
     fields = '__all__'
     