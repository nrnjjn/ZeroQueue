from django.db import models

# Create your models here.
class Cancellation(models.Model):
    c_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    u_id = models.IntegerField()
    department = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cancellation'
        unique_together = (('c_id', 'date', 'time', 'u_id'),)


