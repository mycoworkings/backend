# Generated by Django 2.2.11 on 2020-03-16 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiRest', '0008_contact_socialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='socialMedia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ApiRest.socialMedia'),
        ),
    ]
