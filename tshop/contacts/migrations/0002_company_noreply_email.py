# Generated by Django 2.0.4 on 2018-06-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='noreply_email',
            field=models.EmailField(default='mail@mail.ru', max_length=255),
        ),
    ]