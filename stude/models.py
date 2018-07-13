from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=250)
    grade = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % self.name

    def get_excerpt(self, char):
        return self.name[:char]

    class Meta:
        verbose_name_plural = 'Students'