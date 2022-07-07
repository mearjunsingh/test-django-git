from django import forms
from django.core.exceptions import ValidationError

from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Contact
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        if "@gmail.com" not in email:
            raise ValidationError("email ma gmail xaina")
