# Generated by Django 4.0.3 on 2022-03-09 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currencyapi', '0013_rename_frc_currency_aud_rename_mex_currency_cud_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='CUD',
            new_name='CAD',
        ),
        migrations.RenameField(
            model_name='currency',
            old_name='PLN',
            new_name='RUB',
        ),
    ]
