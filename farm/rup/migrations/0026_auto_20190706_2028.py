# Generated by Django 2.2 on 2019-07-07 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rup', '0025_auto_20190706_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='center',
            name='user',
        ),
        migrations.AddField(
            model_name='center',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
