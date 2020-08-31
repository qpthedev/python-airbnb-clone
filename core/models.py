from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        # Prevent this model from going to the DB
        abstract = True
