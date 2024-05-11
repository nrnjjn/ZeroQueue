from django.db import models

# Create your models here.
class Appointment(models.Model):
    a_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    department = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'appointment'
        unique_together = (('a_id', 'u_id', 'date', 'time'),)
