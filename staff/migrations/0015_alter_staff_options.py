# Generated by Django 4.2 on 2023-04-10 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0014_rename_bb_additionalimage_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['is_published'], 'verbose_name': 'Publication', 'verbose_name_plural': 'Publications'},
        ),
    ]
