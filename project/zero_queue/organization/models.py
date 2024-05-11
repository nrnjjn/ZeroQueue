from django.db import models

# Create your models here.
class ManageOrganization(models.Model):
    o_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    working_hours = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'manage_organization'


