# Generated by Django 3.2.5 on 2021-08-10 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('series', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('completed', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, default=None, upload_to='uploads/')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ToBuyItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('link', models.URLField(blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosyapp.project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('completed', models.BooleanField(default=False)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosyapp.part')),
            ],
        ),
        migrations.AddField(
            model_name='part',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosyapp.project'),
        ),
    ]
