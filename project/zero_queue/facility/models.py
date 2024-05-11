from django.db import models

# Create your models here.

class Facilities(models.Model):
    f_id = models.AutoField(primary_key=True)
    o_id = models.IntegerField()
    facilities = models.CharField(max_length=30)
    details = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'facilities'



