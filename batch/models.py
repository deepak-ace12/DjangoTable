from django.db import models

# Create your models here.

class Batch(models.Model):
    batch_name = models.CharField(max_length=100)
    batch_stream = models.CharField(max_length=100)
    batch_class = models.CharField(max_length=100)
    batch_contact = models.CharField(max_length=100)

    def __str__(self):
        return self.batch_name+' - '+self.batch_stream


class Student(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_contact = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100, default='abc@example.com')
    student_DOB = models.CharField(max_length=100, default='dd/mm//yyyy')
    def __str__(self):
        return self.first_name+' '+self.last_name

