from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='home/banners')
    alt = models.CharField(max_length=20)

    def __str__(self):
        return self.alt
