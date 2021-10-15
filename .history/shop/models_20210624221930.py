from django.db import models

# Create your models here.
class PRODUCT(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)