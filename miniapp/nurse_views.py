from django.shortcuts import redirect, render

from .forms import loginform, nurseform, nurse_updateform, vaccine_scheduleform, v_schedule_updateform
from .models import Nurse, Vaccine_Schedule


def nurse_home(request):
    return render(request, 'nurse_temp/nurse_home.html')




def nurse_register(request):
    if request.method == "POST":
        formlog = loginform(request.POST)
        form_nurse = nurseform(request.POST)
        if formlog.is_valid() and form_nurse.is_valid():
            formlog_save = formlog.save(commit=False)
            formlog_save.is_Nurse = True
            formlog_save.save()

            form_nurse_save = form_nurse.save(commit=False)
            form_nurse_save.login_id = formlog_save
            form_nurse_save.save()
            return redirect('nursetable')
    else:
            formlog = loginform()
            form_nurse = nurseform()
    return render(request, 'nurse_temp/add_nurse_card.html', {"formlogkey": formlog, "form_nursekey": form_nurse})


def nurse_data(request):
    nursedata = Nurse.objects.all()
    return render(request, 'nurse_temp/nurse_table.html', {"nursedatakey": nursedata})

def nurse_delete(request,id=None):
    data=Nurse.objects.get(id=id)
    data.delete()
    return redirect('nursetable')

def nurse_edit(request,id=None):
    data=Nurse.objects.get(id=id)
    if request.method=="POST":
        nurseedit = nurse_updateform(request.POST,instance=data)
        if nurseedit.is_valid():
            nurseedit.save()
            return redirect('nursetable')
    else:
        nurseedit = nurse_updateform(instance=data)
    return render(request,'nurse_temp/nurse_update.html',{"nurseeditkey":nurseedit})

def v_schedule(request):
    if request.method=="POST":
        vs=vaccine_scheduleform(request.POST)
        if vs.is_valid():
            vs.save()
            return redirect('scheduletable')
    else:
        vs=vaccine_scheduleform()
    return render(request,'nurse_temp/v_schedule_form.html',{"vskey":vs})

def v_schedule_data(request):
    scheduledata = Vaccine_Schedule.objects.all()
    return render(request, 'nurse_temp/v_schedule_table.html', {"scheduledatakey": scheduledata})

def v_schedule_delete(request,id=None):
    data=Vaccine_Schedule.objects.get(id=id)
    data.delete()
    return redirect('scheduletable')

def v_schedule_edit(request,id=None):
    data=Vaccine_Schedule.objects.get(id=id)
    if request.method=="POST":
        v_s_edit = v_schedule_updateform(request.POST,instance=data)
        if v_s_edit.is_valid():
            v_s_edit.save()
            return redirect('scheduletable')
    else:
        v_s_edit =v_schedule_updateform(instance=data)
    return render(request,'nurse_temp/v_schedule_update.html',{"v_s_editkey":v_s_edit})