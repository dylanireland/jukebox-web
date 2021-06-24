from django.contrib import admin
from django.urls import path, include
from .models import TaskLogger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('juke.urls')),
]

class TaskAdmin(admin.ModelAdmin):
    fields = [field.name for field in TaskLogger._meta.get_fields()]

admin.site.register(TaskLogger, TaskAdmin)
