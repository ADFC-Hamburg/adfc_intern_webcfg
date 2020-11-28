# Generated by Django 2.2.17 on 2020-11-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenSlidesInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=16)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('admin_name', models.CharField(max_length=20)),
                ('admin_email', models.CharField(max_length=200)),
                ('meet_room', models.CharField(max_length=20)),
            ],
        ),
    ]