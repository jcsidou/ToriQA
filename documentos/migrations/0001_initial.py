# Generated by Django 5.1 on 2024-08-17 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('arquivo', models.FileField(upload_to='pdfs/')),
                ('texto_extraido', models.TextField()),
            ],
        ),
    ]
