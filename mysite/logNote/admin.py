from django.contrib import admin
#runs in reality from server even if error here
from logNote.models import User,Log

# Register your models here.
admin.site.register(User)
admin.site.register(Log)