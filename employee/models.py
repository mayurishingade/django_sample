from django.db import models
from django.core.exceptions import ValidationError

def validate_name(value):
    if type(value)==str and len(value)>=5:
        return value
    else:
        raise ValidationError('Invalid name...')

def validate_email(value):
    if type(value)==str and len(value)>=11 and "@gmail.com":
        return value
    else:
        raise ValidationError('Invalid Email...')




class Employee(models.Model):
    name=models.CharField(max_length=30, validators=[validate_name])
    age =models.IntegerField()
    email=models.CharField(max_length=30, unique=True, validators=[validate_email])
    role = models.CharField(max_length=30, default='Guest')
    phone_num = models.BigIntegerField(unique=True)
    joiningDate = models.DateField()
    address = models.CharField(max_length=255, default='Y')

    class Meta:
        db_table='employee_master'
        ordering=['role']