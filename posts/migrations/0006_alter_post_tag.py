# Generated by Django 4.1.1 on 2022-09-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_tag_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='post_tag', to='posts.tag'),
        ),
    ]
