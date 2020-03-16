# Generated by Django 2.2.11 on 2020-03-16 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiRest', '0006_facebook_instagram_linkedin_socialmedia_twitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='facebook',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ApiRest.facebook'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='instagram',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ApiRest.instagram'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='linkedin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ApiRest.linkedin'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='twitter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ApiRest.twitter'),
        ),
    ]
