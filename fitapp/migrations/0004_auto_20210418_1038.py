# Generated by Django 3.1.2 on 2021-04-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]