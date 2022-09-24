from django.shortcuts import render
from .models import Resume
from .forms import ResumeForm


def index(request):
    if request.method=="POST":
        form = ResumeForm(request.POST)
        form.save()
    form = ResumeForm()
    resume = Resume.objects.all()
    data = {"resume": resume, "form": form }
    return render(request, "initial_comm/index.html",data)
