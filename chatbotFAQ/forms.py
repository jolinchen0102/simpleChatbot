
from django import forms

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

class ContactUsForm(forms.Form):
   name = forms.CharField(required=True)
   category = forms.ChoiceField(choices = RELEVANCE_CHOICES, required=True)
   country = forms.ChoiceField(choices = COUNTRY_CHOICES, required=True)
   question = forms.CharField(max_length=200)