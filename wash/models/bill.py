from django.db import models

from wash.models.user import User
from wash.models.washing_program import WashingProgram


class Bill(models.Model):
    price = models.FloatField()
    price_after_discount = models.FloatField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    washing_program = models.ForeignKey(WashingProgram, on_delete=models.CASCADE)

    def __str__(self):
        return self

    class Meta:
        ordering = ["created_at"]
