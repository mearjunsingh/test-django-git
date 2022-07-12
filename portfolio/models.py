from django.db import models


class Contact(models.Model):
    name = models.CharField("full name", max_length=100)
    email = models.EmailField("email")
    message = models.TextField("message")
    contact_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.email}"
