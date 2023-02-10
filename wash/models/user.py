from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    loyalty_level = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}/{self.email} - {self.loyalty_level} lvl"

    class Meta:
        ordering = ["date_joined"]
