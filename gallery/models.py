from django.db import models

# here is django's orm

class Photo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    subtitle = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)

    def __str__(self):
        return self.title