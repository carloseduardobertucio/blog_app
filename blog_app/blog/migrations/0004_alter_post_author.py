# Generated by Django 4.1 on 2023-05-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_active_alter_comment_name_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=80),
        ),
    ]
