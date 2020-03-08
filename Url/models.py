from django.db import models
from ShortenUrl.utils import unique_order_id_generator

class ShortUrl(models.Model):

    actual_url = models.CharField(max_length=1024, null=False, blank=False)
    short_url = models.CharField(max_length=128, unique=True, null=False, blank=True)

    hits = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.actual_url

    @property
    def url_hits(self):
        return self.hits
    
    @property
    def increment_hit(self):
        print('increment_hit')
        self.hits += 1
        self.save()
    
    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = unique_order_id_generator(ShortUrl)
        super(ShortUrl, self).save(*args, **kwargs) 
