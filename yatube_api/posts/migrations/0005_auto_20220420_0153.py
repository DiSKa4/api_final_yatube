# Generated by Django 2.2.16 on 2022-04-19 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_group'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follow',
        ),
    ]
