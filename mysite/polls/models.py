from django.db import models

# Create your models here.
class info(models.Model):
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    def __str__(self):
        return "%s=>%s=>%s" % (self.username, self.phone,self.info)
