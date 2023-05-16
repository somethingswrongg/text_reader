from django.db import models


class TextReader(models.Model):
    text = models.TextField()
