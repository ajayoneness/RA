# Generated by Django 4.2.1 on 2023-08-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('you', '0004_quotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='poster/'),
        ),
    ]
