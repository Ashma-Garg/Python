from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    # amount = models.DecimalField(max_digits=8, decimal_places=2)    # examlple: 999999.99
    description = models.TextField()
    dob = models.DateField()
    phone = models.CharField(max_length=10)


# for foreign keys
# class Company(models.Model):
#     co_name = models.CharField()

# class Car(models.Model):
#     type = models.CharField()
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)


