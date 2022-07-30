from django.db import models

from presentations.models import Presentation


class PresentationSlot(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    current_page = models.IntegerField(default=1)
    duration = models.DurationField()
    start_time = models.DateTimeField()

    def __str__(self):
        return (
            f"{self.presentation.user}'s presentation at "
            f"{self.start_time:%Y-%m-%d %H:%M}"
        )
