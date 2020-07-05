from django.db import models


# Create your models here.
class UrlsManager(models.Manager):
    def get_or_create(self, query):
        try:
            result = Urls.objects.filter(original_url=query).first()
        except IndexError:
            result = Urls.objects.create(original_url=query)
        return result


class Urls(models.Model):
    original_url = models.TextField()
    shortened_url = models.CharField(max_length=99)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_url}, {self.created_date}"
