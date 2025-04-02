# Generated by Django 5.1.7 on 2025-04-02 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_genre_book_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ReadingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateField()),
                ('state', models.TextField(choices=[('A', 'Chci číst'), ('B', 'Právě čtu')], max_length=1)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('text', models.TextField(blank=True, default='')),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
