from django.db import models
from django.utils.text import slugify

# Create your models here.
class XImage(models.Model):
    id = models.AutoField(primary_key=True)
    pathImage = models.CharField(max_length=100)
    uploader = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pathImage)
        super(XImage, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.id) + " - " + self.pathImage
    
class XSegmentationResult(models.Model):
    id = models.AutoField(primary_key=True)
    idImage = models.ForeignKey(XImage, on_delete=models.CASCADE)
    pathSegmentationKMeans = models.CharField(max_length=100)
    pathSegmentationAdaptive = models.CharField(max_length=100)
    pathGroundTruth = models.CharField(max_length=100)
    # model json 
    report = models.JSONField()
    date = models.DateTimeField(auto_now_add=True)
