from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"
