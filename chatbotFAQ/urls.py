from django.urls import path
from chatbotFAQ import views

urlpatterns = [
	path('hello', views.hello),
	path('contact-us/', views.contact, name='contact'),
 	path('contact-us/question_sent/', views.question_sent, name='question')
]
