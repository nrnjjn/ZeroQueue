from django.db import models

# Create your models here.
class WorkingHours(models.Model):
    w_id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField(db_column='start time')  # Field renamed to remove unsuitable characters.
    department = models.CharField(max_length=50)
    end_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'working_hours'
        unique_together = (('w_id', 'date', 'start_time'),)


