# Generated by Django 3.0.8 on 2020-07-26 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epicApp', '0012_comment_approved_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
