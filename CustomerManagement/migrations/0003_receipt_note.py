# Generated by Django 3.0.3 on 2020-06-27 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerManagement', '0002_auto_20200626_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
