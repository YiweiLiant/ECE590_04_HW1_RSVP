# Generated by Django 2.1.dev20180124004857 on 2018-02-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSVP', '0002_auto_20180207_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_id',
        ),
        migrations.AddField(
            model_name='choice',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
