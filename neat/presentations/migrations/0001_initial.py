# Generated by Django 4.0.6 on 2022-07-29 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import presentations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'pdf'), ('2', 'embed')], max_length=1)),
                ('embed_url', models.URLField(max_length=300)),
                ('pdf_file', models.FileField(upload_to=presentations.models.user_directory_path)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
