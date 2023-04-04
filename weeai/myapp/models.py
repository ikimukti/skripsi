from django.db import models

# Create your models here.
class XImage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    pathImage = models.CharField(max_length=100)
    uploader = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.id) + " - " + self.title

