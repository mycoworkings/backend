# Generated by Django 2.2.11 on 2020-03-16 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiRest', '0007_auto_20200316_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='socialMedia',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ApiRest.socialMedia'),
            preserve_default=False,
        ),
    ]