# Generated by Django 2.2 on 2019-05-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rup', '0007_save'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('verticies', models.TextField()),
            ],
        ),
    ]
