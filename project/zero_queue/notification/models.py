from django.db import models

# Create your models here.
class Notification(models.Model):
    n_id = models.AutoField(primary_key=True)
    date = models.DateField()
    notification = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'notification'

