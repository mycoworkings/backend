# Generated by Django 2.2.11 on 2020-03-16 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiRest', '0012_auto_20200316_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coworking',
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='socialmedia',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='socialmedia',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='socialmedia',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='socialmedia',
            name='twitter',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Coworking',
        ),
        migrations.DeleteModel(
            name='facebook',
        ),
        migrations.DeleteModel(
            name='instagram',
        ),
        migrations.DeleteModel(
            name='linkedin',
        ),
        migrations.DeleteModel(
            name='socialMedia',
        ),
        migrations.DeleteModel(
            name='twitter',
        ),
    ]