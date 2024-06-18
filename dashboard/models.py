from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import os
from uuid import uuid4
from django_resized import ResizedImageField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    addressLine1 = models.CharField(null=True, blank=True, max_length=100)
    addressLine2 = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
    province = models.CharField(null=True, blank=True, max_length=100)
    country = models.CharField(null=True, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=100)
    profileImage = ResizedImageField(size=[200, 200], quality=90, upload_to='profile_images')

    # Utility Variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100, unique=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.email)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4())

        if not self.slug:
            base_slug = slugify('{}-{}-{}'.format(self.user.first_name, self.user.last_name, self.user.email))
            unique_slug = base_slug
            num = 1
            while Profile.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(base_slug, num)
                num += 1
            self.slug = unique_slug

        self.last_updated = timezone.localtime(timezone.now())
        super(Profile, self).save(*args, **kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    keywords = models.CharField(null=True, blank=True, max_length=300)
    wordCount = models.CharField(null=True, blank=True, max_length=100)     
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    # Utility Variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100, unique=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4())

        if not self.slug:
            base_slug = slugify('{} {}'.format(self.title, self.uniqueId))
            unique_slug = base_slug
            num = 1
            while Profile.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(base_slug, num)
                num += 1
            self.slug = unique_slug

        self.last_updated = timezone.localtime(timezone.now())
        super(Blog, self).save(*args, **kwargs) 

class BlogSection(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True) 
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


    # Utility Variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100, unique=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4())

        if not self.slug:
            base_slug = slugify('{} {}'.format(self.title, self.uniqueId))
            unique_slug = base_slug
            num = 1
            while Profile.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(base_slug, num)
                num += 1
            self.slug = unique_slug

        self.last_updated = timezone.localtime(timezone.now())
        super(BlogSection, self).save(*args, **kwargs)         