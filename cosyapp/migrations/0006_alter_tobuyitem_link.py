# Generated by Django 3.2.5 on 2021-07-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosyapp', '0005_alter_project_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tobuyitem',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
