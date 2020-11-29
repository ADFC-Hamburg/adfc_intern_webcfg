# Generated by Django 3.1 on 2020-11-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openslides_cfg', '0004_auto_20201129_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='openslidesinstance',
            name='admin_email',
            field=models.EmailField(default='', max_length=254, verbose_name='E-Mail Addresse des Administrators (admin)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='openslidesinstance',
            name='enable_electronic_voting',
            field=models.BooleanField(default=True, verbose_name='Elektronische Wahlen erlauben'),
        ),
        migrations.AlterField(
            model_name='openslidesinstance',
            name='meet_password',
            field=models.CharField(max_length=40, verbose_name='Jitsi Meet Raumpasswort (sofern vergeben)'),
        ),
        migrations.AlterField(
            model_name='openslidesinstance',
            name='reset_password_verbose',
            field=models.BooleanField(default=True, verbose_name='Aussagekrägtige Fehlermeldung beim Passwort zurücksetzen'),
        ),
    ]