# Generated by Django 3.2.3 on 2021-09-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=20)),
            ],
        ),
    ]
