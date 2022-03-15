from django.contrib.auth.forms import UserCreationForm
from django import forms

from . import models
from .models import Login, Vaccine, Hospital, Nurse, User, Vaccine_Schedule, Appointment


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class loginform(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')

class vaccineform(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ('vaccine_name','vaccine_type','description','approval_status')

class vaccine_updateform(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = '__all__'

class hospitalform(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ('name','place','contact_no','email')

class hospital_updateform(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

class nurseform(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ('name','contact_no', 'address', 'email', 'Hospital')

class nurse_updateform(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = '__all__'

class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name','contact_no', 'address', 'child_name', 'child_age','child_gender','recent_vaccinations')


class vaccine_scheduleform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)
    class Meta:
        model = Vaccine_Schedule
        fields = ('Hospital','date','start_time','end_time')

class v_schedule_updateform(forms.ModelForm):
    class Meta:
        model = Vaccine_Schedule
        fields = '__all__'

class appointment_form(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('user', 'schedule', 'status','vaccine_name', 'vaccinated')