from django.forms import ModelForm
from .models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ["name", "phone", "spec", "adres", "gender", "age", "experience", "skills"]

