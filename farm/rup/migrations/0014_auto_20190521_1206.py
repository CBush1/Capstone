# Generated by Django 2.2 on 2019-05-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rup', '0013_auto_20190517_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='license_no',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Applicator',
        ),
    ]