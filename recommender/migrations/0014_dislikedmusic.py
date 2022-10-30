# Generated by Django 3.2.15 on 2022-10-30 00:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recommender', '0013_album_artist_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='DislikedMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ManyToManyField(blank=True, null=True, to='recommender.Musicdata')),
                ('user', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
