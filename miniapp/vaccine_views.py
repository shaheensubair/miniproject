from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import loginform, vaccineform, vaccine_updateform
from .models import Vaccine

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("admin_home")
            elif user.is_Nurse:
                return redirect("nurse_home")
            elif user.is_User:
                return redirect("user_home")
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'sign_in.html')


def vaccine_form(request):
    if request.method=="POST":
        formlog = loginform(request.POST)
        formvaccine = vaccineform(request.POST)
        if formlog.is_valid() and formvaccine.is_valid():
            formlog_save = formlog.save(commit=False)
            formlog_save.is_vaccine=True
            formlog_save.save()

            formvaccine_save = formvaccine.save(commit=False)
            formvaccine_save.login_id=formlog_save
            formvaccine_save.save()
            return redirect('vaccinetable')
    else:
        formlog = loginform()
        formvaccine = vaccineform()
    return render(request,'vaccine_temp/add_vaccine_card.html',{"formlogkey" : formlog, "formvaccinekey" : formvaccine})

def vaccine_data(request):
    vaccinedata = Vaccine.objects.all()
    return render(request, 'vaccine_temp/vaccine_table.html', {"vaccinedatakey": vaccinedata})




def vaccine_delete(request,id=None):
    data=Vaccine.objects.get(id=id)
    data.delete()
    return redirect('vaccinetable')

def vaccine_edit(request,id=None):
    data=Vaccine.objects.get(id=id)
    if request.method=="POST":
        vaccineedit = vaccine_updateform(request.POST,instance=data)
        if vaccineedit.is_valid():
            vaccineedit.save()
            return redirect('vaccinetable')
    else:
        vaccineedit = vaccine_updateform(instance=data)
    return render(request,'vaccine_temp/vaccine_update.html',{"vaccineeditkey":vaccineedit})
