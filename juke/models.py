from django.db import models

class TaskLogger(models.Model):
    getBlockNumberModel = models.CharField(max_length=36, primary_key=True)
