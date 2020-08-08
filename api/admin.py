from django.contrib import admin

#after creating model, register here. then migrate
from api.models import Task
admin.site.register(Task)
