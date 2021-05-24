from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Ticket)
admin.site.register(models.UserProfile)
admin.site.register(models.Game)
admin.site.register(models.Winner)

