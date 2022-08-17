from django.shortcuts import render, redirect
from django.http import HttpResponse
from chatbotFAQ.forms import ContactUsForm


# Create your views here.
def hello(request):
    return HttpResponse("hello user!")

def question_sent(request):
    return HttpResponse("Your question has been sent, we will get back to you soon!")


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        # print(form.cleaned_datas)
        return redirect('question')
    else:
        form = ContactUsForm()
    return render(request,
          'simpleForm.html',
          {'form': form})