# Generated by Django 3.2.5 on 2021-08-13 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cosyapp', '0003_alter_referencephoto_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referencephoto',
            name='description',
        ),
    ]
