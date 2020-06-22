from django.db import models

# Create your models here.


class Traffic(models.Model):
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.ip
