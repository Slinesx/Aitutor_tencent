# Generated by Django 3.1.7 on 2021-08-31 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionRecord', '0011_commonuser_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level2',
            name='op1',
        ),
        migrations.RemoveField(
            model_name='level2',
            name='op2',
        ),
        migrations.RemoveField(
            model_name='level2',
            name='op3',
        ),
    ]