# Generated by Django 4.0.4 on 2022-06-23 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_personalinformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='experience_years',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='middlename',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='professional',
        ),
    ]