from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import loginform, userform, vaccineform
from .models import User, Vaccine, Vaccine_Schedule, Hospital, Appointment


def user_home(request):
    return render(request, 'user_temp/user_home.html')

def user_register(request):
    if request.method == "POST":
        formlog = loginform(request.POST)
        form_user = userform(request.POST)
        if formlog.is_valid() and form_user.is_valid():
            formlog_save = formlog.save(commit=False)
            formlog_save.is_User = True
            formlog_save.save()

            form_user_save = form_user.save(commit=False)
            form_user_save.login_id = formlog_save
            form_user_save.save()
            return redirect('usertable')
    else:
            formlog = loginform()
            form_user = userform()
    return render(request, 'user_temp/add_user_card.html', {"formlogkey": formlog, "form_userkey": form_user})


def user_data(request):
    userdata = User.objects.all()
    return render(request, 'user_temp/user_table.html', {"userdatakey": userdata})

def user_delete(request,id=None):
    data=User.objects.get(id=id)
    data.delete()
    return redirect('usertable')







def user_profile_data(request):
    user_profile = User.objects.all()
    return render(request, 'user_temp/user_profile_table.html', {"user_profilekey": user_profile})


def user_vaccine_data(request):
    user_vaccine = Vaccine.objects.all()
    return render(request, 'user_temp/user_vaccine_table.html', {"user_vaccinekey": user_vaccine})

def user_vaccine_schedule_data(request):
    user_vaccine_schedule = Vaccine_Schedule.objects.all()
    return render(request, 'user_temp/user_vaccine_schedule_table.html', {"user_vaccine_schedulekey": user_vaccine_schedule})

def user_hospital_data(request):
    user_hospital = Hospital.objects.all()
    return render(request, 'user_temp/user_hospital_table.html', {"user_hospitalkey": user_hospital})











def take_appointment(request, id):
    s = Vaccine_Schedule.objects.get(id=id)
    u = User.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u,schedule=s)
    if appointment.exists():
        messages.info(request, 'You have already requested appointment for this schedule')
        return redirect('uservaccine_scheduletable')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = u
            obj.schedule = s
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('appointment_table')
    return render(request, 'user_temp/appointment_form.html', {'skey':s})








