from django.db import models

# Create your models here.
class PRODUCT(models.Model):
    pro_id = models.AutoField
    pro_name = models.CharField(max_length=50)
    pro_desc = models.CharField(max_length=500)
    publish_date = models.DateField()