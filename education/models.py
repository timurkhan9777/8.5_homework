from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    duration = models.IntegerField()

    def __str__(self):
        return self.name

class Teachers(models.Model):

    STATUS_CHOICES = [
        ('active','Active'),
        ('inactive','Inactive'),
        ('retired','Retired'),
    ]

    full_name = models.CharField(max_length=255)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='active')
    experience = models.IntegerField()
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.full_name


class Students(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    parents_phone = models.CharField(max_length=13)
    telegram_link = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teachers)

    def __str__(self):
        return self.full_name