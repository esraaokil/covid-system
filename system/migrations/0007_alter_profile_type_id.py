# Generated by Django 4.0.4 on 2022-06-24 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_pregnant_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='type_profile', to='system.type'),
        ),
    ]
