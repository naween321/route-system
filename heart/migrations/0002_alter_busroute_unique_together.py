# Generated by Django 4.1.6 on 2023-02-08 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='busroute',
            unique_together={('bus', 'route', 'from_time', 'to_time'), ('bus', 'from_time', 'to_time')},
        ),
    ]
