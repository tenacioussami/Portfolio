from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    technology = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
