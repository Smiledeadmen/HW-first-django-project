from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name}, {self.price}: {self.slug}'