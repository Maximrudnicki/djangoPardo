# Generated by Django 4.1.1 on 2022-09-21 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListOfWordSets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_word_set', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
