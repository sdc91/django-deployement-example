from django.db import models
from django import forms

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=120)
    adress = models.TextField()

class ShoeModelForm(forms.ModelForm):
    class Meta():
        model = Shoe
        fields = "__all__"
