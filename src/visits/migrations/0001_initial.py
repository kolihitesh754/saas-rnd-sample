# Generated by Django 5.0.13 on 2025-03-07 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
