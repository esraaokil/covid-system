# Generated by Django 4.0.4 on 2022-06-25 00:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0013_chestdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chronic_diseases',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('diseases_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
