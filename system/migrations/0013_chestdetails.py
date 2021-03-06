# Generated by Django 4.0.4 on 2022-06-25 00:14

from django.db import migrations, models
import django.db.models.deletion
import system.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0012_remove_profile_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChestDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('x_ray_image', models.ImageField(blank=True, null=True, upload_to=system.models.upload_to)),
                ('status', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=10)),
                ('regestration_date', models.DateTimeField(auto_now_add=True)),
                ('patient_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_x_ray', to='system.patient')),
            ],
        ),
    ]
