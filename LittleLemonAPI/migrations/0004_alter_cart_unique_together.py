# Generated by Django 4.2.7 on 2023-12-01 15:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LittleLemonAPI', '0003_rename_menuitem_cart_menuitems_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'menuitems')},
        ),
    ]