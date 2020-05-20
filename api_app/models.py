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
    quote = models.TextField()
    date_created = models.DateTimeField(datetime.now())
    
    def __str__(self):
        return '{} quote created {}'.format(self.sin.capitalize(), self.date_created)