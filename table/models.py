from django.db import models

class Usr(models.Model):
    nicname = models.CharField('никнейм', max_length=20)
    email = models.CharField('email', max_length=50)
    name = models.CharField('имя пользователя', max_length=50)

    def __str__(self):
        return self.name

class Tabletop(models.Model):
    title = models.CharField('название стола', max_length=50)
    description = models.TextField('описание стола')
    owner = models.ForeignKey(Usr, related_name='owner', on_delete=models.CASCADE)
    players = models.ManyToManyField(Usr, related_name='players')
    GAME_SYSTEMS = {
        ('HONEYHEIST', "Honey heist"),
        ('CRASHPANDAS', "Crash pandas"),
    }
    gameSystem = models.CharField(
        'игровая система',
        max_length=50, 
        choices=GAME_SYSTEMS,
        default='HONEYHEIST')
        
    def __str__(self):
        return self.title