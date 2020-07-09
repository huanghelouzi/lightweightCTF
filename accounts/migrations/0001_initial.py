# Generated by Django 2.0 on 2020-04-05 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('teamname', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('job', models.CharField(default='', max_length=100, null=True)),
                ('company', models.CharField(default='', max_length=250, null=True)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
    ]
