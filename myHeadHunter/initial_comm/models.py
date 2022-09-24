from django.db import models


class Resume(models.Model):
    name = models.CharField("name", max_length=20)
    gender = models.CharField("gender", max_length=1, choices=(("ж", "ж"), ("м", "м")), default="")
    phone = models.CharField("phone", max_length=20)
    age = models.CharField("age", max_length=3)
    spec = models.CharField("spec", max_length=20)
    option = (("Полная", "Полная"), ("Частичная", "Частичная"), ("Удалённо", "Удалённо"))
    type_of_employment = models.CharField("type_of_employment", max_length=20, choices=option, default="")
    adres = models.CharField("adres", max_length=50, default="")
    experience = models.TextField("experience", default="")
    skills = models.TextField("skills", default="")
    confirm_skills = models.TextField("confirm_skills",max_length=50, default="")
    salary = models.CharField("salary",max_length=150,default="")
