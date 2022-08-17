from cProfile import label
from unicodedata import category
from django.db import models
from multiselectfield import MultiSelectField

RELEVANCE_CHOICES = (
    (1, "KYC onboarding"),
    (2, "Funding features"),
    (3, "Trading features"),
    (4, "Custody features"),
    (5, "Fee schedule"),
    (6, "Security"),
    (7, "Others"),
)
COUNTRY_CHOICES = (
    (1, "China"),
    (2, "Singapore"),
    (3, "United Kingdom"),
    (4, "United States")
)
# Create your models here.
class Question(models.Model):
    name = models.fields.CharField(max_length=100) 
    category = MultiSelectField(choices=RELEVANCE_CHOICES,
                                 max_choices=1,
                                 max_length=1
                                 )
    country = MultiSelectField(choices=COUNTRY_CHOICES,
                                 max_choices=1,
                                 max_length=1
                                 )
    question = models.fields.CharField(max_length=200)
    def __str__(self):
        return self.question

