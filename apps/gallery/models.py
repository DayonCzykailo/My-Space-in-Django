from django.db import models

# here is django's orm

class Photo(models.Model): 
    CATEGORY_CHOICES = (
        ("NEBULOUS", "Nebulous"),
        ("STARS", "Stars"),
        ("GALAXIES", "Galaxies"),
        ("PLANETS", "Planets"),
        ("COMETS", "Comets"),
        ("METEORS", "Meteors"),
        ("ASTEROIDS", "Asteroids"),
        ("OTHERS", "Others")
    )


    title = models.CharField(max_length=100, blank=False, null=False)
    subtitle = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=False, null=False, default='OTHERS')
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    published = models.BooleanField(default=False)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='user')

    def __str__(self):
        return self.title