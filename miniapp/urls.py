from django.urls import path

from . import views, admin_views, vaccine_views, hospital_views, nurse_views, user_views

urlpatterns = [

    path('sign_up/', admin_views.sign, name='sign_up'),
    path('admin_home/',admin_views.admin_home,name='admin_home'),
    path('user_home/',user_views.user_home,name='user_home'),


    path('',views.cover_page,name='cover page'),


    path('my_sign/', vaccine_views.login_view, name="my_sign"),

    path('nurse_signpage/', admin_views.nurse_my_sign, name="nurse_signpage"),
    path('user_signpage/', admin_views.user_my_sign, name="user_signpage"),


    path('vaccine_reg/',vaccine_views.vaccine_form,name='vaccine_reg'),
    path('vaccinetable/',vaccine_views.vaccine_data,name='vaccinetable'),
    path('vaccinedel/<int:id>',vaccine_views.vaccine_delete,name="vaccinedel"),
    path('v_update/<int:id>',vaccine_views.vaccine_edit,name="v_update"),

    path('hospital_reg/', hospital_views.hospital_form, name="hospital_reg"),
    path('hospitaltable/', hospital_views.hospital_data, name="hospitaltable"),
    path('hospitaldel/<int:id>', hospital_views.hospital_delete, name="hospitaldel"),
    path('h_update/<int:id>', hospital_views.hospital_edit, name="h_update"),

    path('nurse_page/', nurse_views.nurse_home, name="nurse_page"),
    path('nurse_reg/', nurse_views.nurse_register, name="nurse_reg"),
    path('nursetable/', nurse_views.nurse_data, name="nursetable"),
    path('nursedel/<int:id>', nurse_views.nurse_delete, name="nursedel"),
    path('n_update/<int:id>', nurse_views.nurse_edit, name="n_update"),

    path('schedule/', nurse_views.v_schedule, name="schedule"),
    path('scheduletable/', nurse_views.v_schedule_data, name="scheduletable"),
    path('v_scheduledel/<int:id>', nurse_views.v_schedule_delete, name="v_scheduledel"),
    path('v_scheduleupdate/<int:id>', nurse_views.v_schedule_edit, name="v_scheduleupdate"),



    path('user_reg/', user_views.user_register, name="user_reg"),
    path('usertable/', user_views.user_data, name="usertable"),
    path('userdel/<int:id>', user_views.user_delete, name="userdel"),


    path('userprofile/', user_views.user_profile_data, name="userprofile"),
    path('uservaccinetable/', user_views.user_vaccine_data, name="uservaccinetable"),
    path('uservaccine_scheduletable/', user_views.user_vaccine_schedule_data, name="uservaccine_scheduletable"),
    path('userhospitaltable/', user_views.user_hospital_data, name="userhospitaltable"),

    path('appointment_reg/<int:id>', user_views.take_appointment, name="appointment_reg"),




]