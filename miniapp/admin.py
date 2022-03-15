from django.contrib import admin

from .models import Login, Vaccine, Hospital, Nurse, User, Vaccine_Schedule, Appointment

admin.site.register(Login)
admin.site.register(Vaccine)
admin.site.register(Hospital)
admin.site.register(Nurse)
admin.site.register(User)
admin.site.register(Vaccine_Schedule)
admin.site.register(Appointment)

