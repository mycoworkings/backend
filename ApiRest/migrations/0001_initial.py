# Generated by Django 2.2.9 on 2020-03-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WebUrl', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coworking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact', models.ManyToManyField(to='ApiRest.Contact')),
            ],
        ),
    ]