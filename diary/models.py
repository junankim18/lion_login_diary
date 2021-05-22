from django.db import models


class Diary(models.Model):
    title = models.CharField(verbose_name='제목', max_length=100)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='diary/', blank=True, null=True)

    def __str__(self):
        return self.title
