# Generated by Django 5.2.2 on 2025-06-05 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0009_alter_review_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='grade',
            new_name='rating',
        ),
    ]
