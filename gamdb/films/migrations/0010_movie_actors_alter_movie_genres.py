# Generated by Django 4.2.2 on 2023-06-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("films", "0009_alter_comment_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(blank=True, to="films.actor"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(blank=True, to="films.genre"),
        ),
    ]
