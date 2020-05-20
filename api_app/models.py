from django.db import models
from datetime import datetime

class SinQuote(models.Model):
    SINS = (
        ('gluttony', 'Gluttony'),
        ('lust', 'Lust'),
        ('greed', 'Greed'),
        ('pride', 'Pride'),
        ('sloth', 'Sloth'),
        ('wrath', 'Wrath'),
        ('envy', 'Envy')
    )

    sin = models.CharField(max_length=8, choices=SINS)
    quote = models.TextField(unique=True, null=False)
    
    def __str__(self):
        return '{} quote'.format(self.sin.capitalize())