# Generated by Django 3.1.5 on 2021-01-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='articles/'),
        ),
    ]
