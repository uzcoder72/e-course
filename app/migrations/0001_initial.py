# Generated by Django 5.0.7 on 2024-07-31 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='authors/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Junior', 'Junior'), ('Middle ', 'Middle'), ('Senior', 'Senior'), ('Expert', 'Expert')], default='Junior', max_length=100)),
                ('twitter_link', models.CharField(blank=True, max_length=150, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=150, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='teachers/')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('auther_id', models.ManyToManyField(related_name='blogs', to='app.author')),
            ],
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.blog')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('number_of_students', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField()),
                ('duration', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/')),
                ('video', models.FileField(upload_to='videos/courses')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='app.category')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('comment', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('rating', models.CharField(choices=[('0', 'Zero'), ('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], default='0', max_length=100)),
                ('written', models.DateTimeField(auto_now_add=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.author')),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.blog')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.course')),
            ],
        ),
    ]
