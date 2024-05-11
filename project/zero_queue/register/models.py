from django.db import models

# Create your models here.
class Register(models.Model):
    u_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(db_column='date of birth')  # Field renamed to remove unsuitable characters.
    age = models.IntegerField()
    gender = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    guardian = models.CharField(max_length=30)
    phone_number = models.CharField(db_column='phone number', max_length=30)  # Field renamed to remove unsuitable characters.
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'register'


