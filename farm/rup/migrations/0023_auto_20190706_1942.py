# Generated by Django 2.2 on 2019-07-07 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rup', '0022_auto_20190705_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='center',
            name='user_center',
        ),
        migrations.AddField(
            model_name='center',
            name='lat',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='lng',
            field=models.TextField(null=True),
        ),
    ]