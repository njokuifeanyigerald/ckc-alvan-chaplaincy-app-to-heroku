from django.contrib import admin
from .models import Baptism,Marriage, Reading,Annoucement
# Register your models here.
admin.site.register(Baptism)
admin.site.register(Marriage)
admin.site.register(Reading)
admin.site.register(Annoucement)