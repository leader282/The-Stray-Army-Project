# Generated by Django 4.1.1 on 2022-10-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0004_story"),
    ]

    operations = [
        migrations.AddField(
            model_name="story",
            name="heading",
            field=models.CharField(default=None, max_length=20000),
        ),
    ]
