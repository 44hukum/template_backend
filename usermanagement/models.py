from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.name)