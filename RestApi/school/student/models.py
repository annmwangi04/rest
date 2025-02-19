from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    adm_number = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):  # ✅ Fixed: Remove space in `__str__`
        return f"{self.first_name} {self.last_name}"  # ✅ Return a readable name
