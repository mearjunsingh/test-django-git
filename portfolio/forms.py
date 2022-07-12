import random

from django import forms
from django.core.exceptions import ValidationError

from .models import Contact


def random_num_generator():
    return random.randint(1, 100)


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
        help_text="use real name",
    )

    a = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        initial=random_num_generator(),
        disabled=True,
    )
    b = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        initial=random_num_generator(),
        disabled=True,
    )
    c = forms.IntegerField(
        label="A + B?", widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Contact
        fields = ["name", "email", "message", "a", "b"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        message = cleaned_data.get("message")
        a = cleaned_data.get("a")
        b = cleaned_data.get("b")
        c = cleaned_data.get("c")

        if a and b and c:
            a = int(a)
            b = int(b)
            c = int(c)
            if (a + b) != c:
                self.add_error(None, ValidationError("Captcha not solved."))

        self.add_error(None, "yo non field error ho")
        self.add_error(None, "yo non field error ho 2")

        # if email:
        #     if Contact.objects.filter(email=email).exists():
        #         self.add_error('email', 'user email already xa')

        # if "Doe" not in name:
        #     # raise ValidationError("name ma doe xaina")
        #     self.add_error("name", "name ma doe xaina")

        # if "John" not in name:
        #     # raise ValidationError("name ma john xaina")
        #     self.add_error("name", ValidationError("name ma john xaina"))
