from django.db import models

# Create your models here.
class Todo (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    date_created = models.DateField(auto_now=True, auto_created=True)

    def __str__(self):
        return  '{title: %s, description: %s, is_done: %s, date_created: %s}' % (self.title, self. description, self. is_done, self. date_created)
    

