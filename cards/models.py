from django.db import models

# Create your models here.


class Card(models.Model):
    Name = models.CharField(max_length=120)
    # mana = models.CharField(max_length=20)

    Abitities = models.CharField(max_length=120)
    Text =  models.TextField()
    Flavor_text = models.TextField()
    Card_Number = models.CharField(max_length=120)
    Artist = models.CharField(max_length=120)
    # spell_type

    CREATURE = 'CR'
    PLANESWALKER = 'PL'
    INSTANT = 'IN'
    SORCERY = 'SO'
    ENCHANTMENT = 'EN'
    ARTIFACT = 'AR'
    SPELL_TYPE = [
        (CREATURE, 'Creature'),
        (PLANESWALKER, 'Planeswalker'),
        (INSTANT, 'Instant'),
        (SORCERY, 'Sorcery'),
        (ENCHANTMENT, 'Enchantment'),
        (ARTIFACT, 'Artifact'),
    ]
    spell_type = models.CharField(
        max_length=2,
        choices=SPELL_TYPE,
        default=CREATURE
    )

    def is_upperclass(self):
        return self.spell_type in ()

