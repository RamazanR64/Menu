from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('menu:menu_item', kwargs={'menu_id': self.id})

    def __str__(self):
        return self.title
