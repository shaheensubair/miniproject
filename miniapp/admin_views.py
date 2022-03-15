from django.shortcuts import render, redirect

from .forms import loginform, nurseform, userform


def sign(request):
    return render(request, 'sign_in.html')

def admin_home(request):
    return render(request, 'admin_temp/admin_home.html')

def nurse_my_sign(request):
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
            return redirect('nurse_signpage')
    else:
            formlog = loginform()
            form_nurse = nurseform()
    return render(request, 'nurse_temp/nurse_form.html', {"formlogkey": formlog, "form_nursekey": form_nurse})


def user_my_sign(request):
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
            return redirect('user_signpage')
    else:
            formlog = loginform()
            form_user = userform()
    return render(request, 'user_temp/user_form.html', {"formlogkey": formlog, "form_userkey": form_user})
