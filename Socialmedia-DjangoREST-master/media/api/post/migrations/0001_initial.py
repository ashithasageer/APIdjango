# Generated by Django 3.2.4 on 2021-06-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('images', models.ImageField(blank=True, default=list, null=True, upload_to='images/')),
                ('tags', models.CharField(blank=True, default=list, max_length=50, null=True)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('dislikes', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
