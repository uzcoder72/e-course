# Generated by Django 5.0.7 on 2024-07-31 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blog_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogImage',
        ),
    ]