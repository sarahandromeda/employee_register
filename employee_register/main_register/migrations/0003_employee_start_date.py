# Generated by Django 4.0.6 on 2022-07-28 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_register', '0002_alter_department_deparment_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]