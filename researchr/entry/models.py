from django.db import models
from uuidfield import UUIDField
from django.contrib.auth.models import User
from django.forms import ModelForm

class Entry(models.Model):
    id = UUIDField(auto=True, primary_key=True)
    title = models.CharField(max_length=512, help_text='Maximum 512 characters.')
    author = models.CharField(max_length=512, help_text='Maximum 512 characters.', blank=True)
    description = models.TextField(blank=True)
    search_text = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="upload", blank=True)
    local_url = models.FileField(upload_to="upload", blank=True)
    remote_url = models.URLField(unique=True, blank=True)
    created_by = models.ForeignKey(User, related_name='entries_created_set')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='entries_updated_set')
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
	ordering = ['title']
	verbose_name_plural = 'Entries'

    class Admin:
	pass

    def __unicode__(self):
	return self.title

    def get_absolute_url(self):
	return "/entries/%s/" % self.id

class EntryForm(ModelForm):
    class Meta:
	model = Entry
