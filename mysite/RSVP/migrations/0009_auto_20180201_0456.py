# Generated by Django 2.1.dev20180124004857 on 2018-02-01 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSVP', '0008_auto_20180201_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
