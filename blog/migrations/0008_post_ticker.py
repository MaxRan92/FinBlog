# Generated by Django 3.2.13 on 2022-05-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_stockticker'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ticker',
            field=models.CharField(default='tbd', max_length=6, unique=True),
            preserve_default=False,
        ),
    ]