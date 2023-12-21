from django.db import models


class BotAdmins(models.Model):
    tg_nickname = models.CharField(max_length=64)
