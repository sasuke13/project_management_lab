from django.db import models


class BotAdmins(models.Model):
    tg_nickname = models.CharField(max_length=64)

    class Meta:
        app_label = 'core'  # Make sure this matches the app name the model belongs to
