# Generated by Django 3.2.15 on 2022-11-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0026_alter_artist_artist_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artist_id',
            field=models.TextField(default=168178892086, primary_key=True, serialize=False),
        ),
    ]
