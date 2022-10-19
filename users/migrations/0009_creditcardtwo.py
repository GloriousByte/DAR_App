# Generated by Django 3.0.3 on 2020-05-25 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_creditcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCardTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_Name', models.CharField(default='1000gh', max_length=150)),
                ('Bank_UC', models.CharField(default='1000gh', max_length=150)),
                ('Card_Number', models.CharField(default='0000', max_length=150)),
                ('CUL', models.CharField(default='0000', max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]