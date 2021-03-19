from django.db import models

from django.contrib.auth import get_user_model

# !!! created with snippet, add properties and alter __str__ as needed
class Deck(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    league = models.CharField(max_length=32)
    size = models.IntegerField()
    mana_type = models.CharField(max_length=32)
    # future  feature, list of cards? ea. card has own table. 
    

    def __str__(self):
         return self.name



