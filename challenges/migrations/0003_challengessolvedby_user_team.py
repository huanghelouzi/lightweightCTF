# Generated by Django 2.0 on 2020-05-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_challengessolvedby_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengessolvedby',
            name='user_team',
            field=models.CharField(default='test', max_length=250),
            preserve_default=False,
        ),
    ]
