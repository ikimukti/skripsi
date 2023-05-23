from django.db import models
from django.utils.text import slugify
class XImage(models.Model):
    id = models.AutoField(primary_key=True)
    nameImage = models.CharField(max_length=100, blank=True, null=True)
    pathImage = models.CharField(max_length=100)
    uploader = models.CharField(max_length=100, blank=True, null=True)
    scaleRatio = models.CharField(max_length=100, blank=True, null=True)
    contrastEnhancement = models.CharField(max_length=100, blank=True, null=True)
    backgroundDominant = models.CharField(max_length=100, blank=True, null=True)
    noiseReduction = models.CharField(max_length=100, blank=True, null=True)
    sizeImage = models.JSONField(null=True)
    distanceObject = models.CharField(max_length=100, blank=True, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150, blank=True, editable=False)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pathImage)
        super(XImage, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.id) + " - " + self.pathImage
    
class XSegmentationResult(models.Model):
    id = models.AutoField(primary_key=True)
    idImage = models.ForeignKey(XImage, on_delete=models.CASCADE)
    pathPreprocessing = models.JSONField(
        null=True
    )
    pathSegmentationResult = models.JSONField(
        null=True
    )
    # model json 
    report = models.JSONField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
