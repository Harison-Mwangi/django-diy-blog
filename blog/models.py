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

class Post(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=100)

    # Foreign Key used because a blog post can only have one blogger, but bloggers can have multiple blog posts
    blogger = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateField(default=date.today, help_text="Date when the post was uploaded")
    description = models.TextField(max_length=4000, help_text='Enter the content for the blog post')
        
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog post."""
        return reverse('post-detail', args=[str(self.id)])