from django.urls import path, include
from .api_views import *
from chatbotFAQ import api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'question', QuestionViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('question/create', question_create, name='questions'),
 	# path('question/', question_list, name='contact'),
  	# path('questions/<int:id>/', views.question_get, name='questions_get'),
 	path('questions/question_sent/', question_sent, name='sent')
]
