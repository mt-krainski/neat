from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"uploads/{instance.user.id}/{filename}"


class Presentation(models.Model):
    class PresentationType(models.TextChoices):
        PDF = "1", "pdf"
        EMBED = "2", "embed"

    type = models.CharField(max_length=1, choices=PresentationType.choices)
    title = models.CharField(max_length=100)
    embed_url = models.URLField(max_length=300, null=True, blank=True)
    pdf_file = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'"{self.title}" by {self.user}'
