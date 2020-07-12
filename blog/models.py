from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from datetime import date

class Blogger(models.Model):
    """Model representing a blogger."""
    name = models.CharField(max_length=25)
    bio = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular blogger instance."""
        return reverse('blogger-detail', args=[str(self.id)])

class Blog(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=100)

    # Foreign Key used because a blog post can only have one author, but bloggers can have multiple posts
    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateField(auto_now_add=True)
    last_edit = models.DateField(auto_now=True)
    description = models.TextField(max_length=4000, help_text='Enter the content for the blog post')

    class Meta:
        ordering = ['-date_posted']
        
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog post."""
        return reverse('blog-detail', args=[str(self.id)])

class Comment(models.Model):
    """Model representing a blog comment."""
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateField(auto_now_add=True)
    last_edit = models.DateField(auto_now=True)
    description = models.TextField(max_length=500, help_text='Enter a comment about the blog post here')

    class Meta:
        ordering = ['-date_posted']
        
    def __str__(self):
        """String for representing the Model object."""
        return self.description[:75]