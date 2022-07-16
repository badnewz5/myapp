# Generated by Django 4.0.4 on 2022-06-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='joptype',
            field=models.CharField(choices=[('Internship', 'Internship'), ('Parttime', 'Parttime'), ('Freelance', 'Freelance'), ('Fulltime', 'Fulltime'), ('Contracted', 'Contracted')], max_length=100, null=True),
        ),
    ]
