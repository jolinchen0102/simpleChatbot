from django.shortcuts import render, redirect
from django.http import HttpResponse
from chatbotFAQ.forms import QuestionForm
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            print(question)
            return redirect('sent')
    else:
        form = QuestionForm()

    return render(
		request,
        'simpleForm.html',
        {'form': form}
	)
   
@api_view(['GET',])
def question_list(request):
    all_questions = Question.objects.all()
    return Response({'All questions': all_questions})
   
def question_sent(request):
    return HttpResponse("Your question has been sent, we will get back to you soon!")

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer