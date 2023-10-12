# Generated by Django 3.2.8 on 2023-05-13 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='familymemb',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('member', models.CharField(max_length=100, verbose_name='Member')),
                ('imagen', models.ImageField(null=True, upload_to='images/', verbose_name='Image')),
                ('description', models.TextField(null=True, verbose_name='Description')),
            ],
        ),
    ]
