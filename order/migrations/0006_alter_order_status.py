# Generated by Django 4.2.3 on 2023-08-09 07:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0005_remove_orderproduct_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("order placed", "order placed"),
                    ("shipped", "shipped"),
                    ("Deliverd", "Deliverd"),
                    ("Cancel", "Cancel"),
                ],
                default="Order Pending",
                max_length=15,
            ),
        ),
    ]