from django.db import models


class WashingStep(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ["type"]
