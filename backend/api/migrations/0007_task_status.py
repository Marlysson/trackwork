# Generated by Django 3.0.8 on 2020-08-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200809_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('STOPPED', 'Stopped'), ('WORKING', 'Working')], default=None, max_length=7),
            preserve_default=False,
        ),
    ]
