# Generated by Django 4.2.1 on 2023-08-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('you', '0006_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]