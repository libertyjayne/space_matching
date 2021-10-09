import uuid
import os
from django.db import models
from utils.models import (AbstractTableMeta)
from django.conf import settings


def space_image_file_path(instance, filename):
    """Generate file path for new space image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/space/', filename)


# class UsLocation(models.Model):
#     address_1 = models.CharField(_("address"), max_length=128)
#     address_2 = models.CharField(
#         _("address cont'd"), max_length=128, blank=True)

#     city = models.CharField(_("city"), max_length=64, default="Zanesville")
#     state = USStateField(_("state"), default="OH")
#     zip_code = models.CharField(_("zip code"), max_length=5, default="43701")


class Space(AbstractTableMeta, models.Model):
    """Space object"""
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
    )
    company = models.CharField(max_length=255, blank=True)
    max_people = models.IntegerField()
    min_people = models.IntegerField()
    max_price = models.DecimalField(max_digits=7, decimal_places=2)
    min_price = models.DecimalField(max_digits=7, decimal_places=2)
    days_per_week = models.IntegerField()
    link = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
      null=True,
      blank=True,
      upload_to=space_image_file_path)
    has_place = models.BooleanField()

    def __str__(self):
        return self.title
