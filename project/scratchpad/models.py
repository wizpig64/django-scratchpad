from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from markdown_deux.templatetags.markdown_deux_tags import markdown_allowed
from datetime import timedelta

class Note(models.Model):
    UPDATED_THRESHOLD = timedelta(minutes=5)

    title = models.CharField(max_length=1024)
    author = models.ForeignKey('auth.User')

    slug = models.SlugField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    body = models.TextField(help_text=markdown_allowed())

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-pk']

    def __unicode__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            if not self.slug:
                slug_length = self._meta.get_field_by_name('slug')[0].max_length
                self.slug = slugify(self.title)[:slug_length]
        super(Note, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def is_updated(self):
        return (self.date_updated - self.date) > self.UPDATED_THRESHOLD
