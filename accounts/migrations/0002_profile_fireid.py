# Generated by Django 3.2.11 on 2022-07-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fireid',
            field=models.CharField(blank=True, default='null', max_length=128, null=True),
        ),
    ]
