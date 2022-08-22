from django.db import models


class LandingPageEntry(models.Model):
    name = models.CharField(max_length=220, blank=True)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}"