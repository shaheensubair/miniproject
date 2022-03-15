from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_Nurse = models.BooleanField(default=False)
    is_User = models.BooleanField(default=False)


class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=50)
    vaccine_type = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    approval_status = models.CharField(max_length=50)

class Hospital(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    email = models.EmailField()

class Nurse(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=50)
    email = models.EmailField()
    Hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=50)
    child_name = models.CharField(max_length=50)
    child_age = models.IntegerField()
    child_gender = models.CharField(max_length=50)
    recent_vaccinations = models.CharField(max_length=50)

class Vaccine_Schedule(models.Model):
    Hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(Vaccine_Schedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    vaccine_name = models.ForeignKey(Vaccine, on_delete=models.DO_NOTHING)
    vaccinated = models.BooleanField(default=False)


