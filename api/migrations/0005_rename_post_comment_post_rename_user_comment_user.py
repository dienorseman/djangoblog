# Generated by Django 4.1.2 on 2022-11-03 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="Post",
            new_name="post",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="User",
            new_name="user",
        ),
    ]