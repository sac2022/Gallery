from datetime import datetime

from django.db import models


# Create your models here.

# def upload_image(filename):
#    return "/{filename}".format(filename=filename)


class ImageModel(models.Model):
    title = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to="Img/%Y/%M/%d")
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title + '' + self.category

    def __unicode__(self):
        return self.image

    def __repr__(self):
        return self.__str__()
