# Generated by Django 3.0.3 on 2020-05-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_amount_owedtolls'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Name',
            field=models.CharField(default='Orange Lake', max_length=150),
        ),
    ]
