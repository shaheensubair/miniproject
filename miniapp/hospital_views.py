from django.shortcuts import redirect, render

from .forms import loginform, hospitalform, hospital_updateform
from .models import Hospital


def hospital_form(request):
    if request.method=="POST":
        formlog = loginform(request.POST)
        formhospital = hospitalform(request.POST)
        if formlog.is_valid() and formhospital.is_valid():
            formlog_save = formlog.save(commit=False)
            formlog_save.is_hospital=True
            formlog_save.save()

            formhospital_save = formhospital.save(commit=False)
            formhospital_save.login_id=formlog_save
            formhospital_save.save()
            return redirect('hospitaltable')
    else:
        formlog = loginform()
        formhospital = hospitalform()
    return render(request,'hospital_temp/add_hospital_card.html',{"formlogkey" : formlog, "formhospitalkey" : formhospital})

def hospital_data(request):
    hospitaldata = Hospital.objects.all()
    return render(request, 'hospital_temp/hospital_table.html', {"hospitaldatakey": hospitaldata})




def hospital_delete(request,id=None):
    data=Hospital.objects.get(id=id)
    data.delete()
    return redirect('hospitaltable')

def hospital_edit(request,id=None):
    data=Hospital.objects.get(id=id)
    if request.method=="POST":
        hospitaledit = hospital_updateform(request.POST,instance=data)
        if hospitaledit.is_valid():
            hospitaledit.save()
            return redirect('hospitaltable')
    else:
        hospitaledit = hospital_updateform(instance=data)
    return render(request,'hospital_temp/hospital_update.html',{"hospitaleditkey":hospitaledit})
