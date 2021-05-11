from django.db import models


class TimeStampMixin(models.Model):
    "determins when model was created and edited"
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """
        declearing abstract class allows class attributes to be used as fields
        when inherited
        """

        abstract = True


class AbstractProfileMixin(models.Model):
    country_code = models.CharField(max_length=3)
    number = models.CharField(max_length=10)
    country = models.CharField(max_length=250)

    class Meta:
        abstract = True
