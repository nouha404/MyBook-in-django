# Generated by Django 4.0.6 on 2022-07-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Titre')),
                ('description', models.TextField(verbose_name='Description')),
                ('publier', models.BooleanField(blank=True)),
            ],
        ),
    ]
