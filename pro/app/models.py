from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
