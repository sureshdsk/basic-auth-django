from django.db import models

class Page(models.Model):
    page_title = models.CharField(max_length=200)
    page_slug = models.SlugField()
    published_date = models.DateTimeField('date published')
    page_content = models.TextField()
    is_private = models.BooleanField(default=False)

    def __unicode__(self):
        return self.page_title