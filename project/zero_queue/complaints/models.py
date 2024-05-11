from django.db import models

# Create your models here.
class Complaints(models.Model):
    c_id = models.AutoField(primary_key=True)

    u_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    complaint = models.CharField(max_length=50)
    reply = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'complaints'

