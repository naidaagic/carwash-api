from django.db import models

from wash.models.washing_step import WashingStep


class WashingProgram(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    washing_steps = models.ManyToManyField(WashingStep)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]
