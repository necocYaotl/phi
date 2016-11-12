from django.db import models

class Posts(models.Model):
    """docstring for posts."""
    headline = models.CharField(max_length = 200)
    main_text = models.TextField()
    post_date = models.DateTimeField('date published')

    def __str__(self):
        return self.headline
