# Generated by Django 4.1.1 on 2022-09-28 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_post_tag'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='posttag',
            table='post_tag',
        ),
    ]