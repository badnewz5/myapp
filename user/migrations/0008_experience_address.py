# Generated by Django 4.0.4 on 2022-06-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_experience_joptype'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
