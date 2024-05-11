from django.db import models

# Create your models here.
class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    o_id = models.IntegerField()
    department = models.CharField(max_length=30)
    details = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'department'


