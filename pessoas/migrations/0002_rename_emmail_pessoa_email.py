# Generated by Django 4.1 on 2022-08-09 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='emmail',
            new_name='email',
        ),
    ]