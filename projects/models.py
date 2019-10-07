from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    summary = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    url = models.URLField(default='https://github.com/Zabamund/')

    def __str__(self):
        return self.title

    def summary(self):
        text_list = self.body.split()
        return ' '.join(text_list[:20]) + ' [...]'

    def create_date_short(self):
        short_time = self.create_date
        return short_time.strftime("%b %d, %Y")