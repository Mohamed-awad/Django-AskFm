# Generated by Django 2.1.4 on 2018-12-17 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20181217_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, default=''),
        ),
    ]