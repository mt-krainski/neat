from django.db import models, transaction

from presentations.models import Presentation


class PresentationSlot(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    current_page = models.IntegerField(default=1)
    duration = models.DurationField()
    start_time = models.DateTimeField()
    active = models.BooleanField()

    def save(self):
        if not self.active:
            return super().save()
        # If this is the active presentation, we want to deactivate all the other ones.
        with transaction.atomic():
            PresentationSlot.objects.exclude(id=self.id).update(active=False)
            super().save()

    def __str__(self):
        return (
            f"{self.presentation.user}'s presentation at "
            f"{self.start_time:%Y-%m-%d %H:%M}"
        )
