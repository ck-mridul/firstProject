# Generated by Django 4.2.3 on 2023-07-25 18:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0005_alter_productimage_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productvariant",
            old_name="storeage",
            new_name="storage",
        ),
    ]