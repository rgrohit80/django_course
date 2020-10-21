from django.db import models


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')

    def roll_range(self, ll, ul):
        return super().get_queryset().filter(roll__range=(ll, ul))
