from django.shortcuts import render
from .models import Resume
from .forms import ResumeForm


def index(request):
    resume = Resume.objects.all()
    data = {"resume": resume, }
    return render(request, "initial_comm/index.html",data)

def send_resume(request):
    if request.method=="POST":
        form = ResumeForm(request.POST)
        form.save()
    form = ResumeForm()
    context = {"form": form}
    return render(request, "initial_comm/send_resume.html", context)
