# Generated by Django 2.1.dev20180124004857 on 2018-02-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSVP', '0003_auto_20180207_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
