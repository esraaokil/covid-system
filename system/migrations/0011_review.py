# Generated by Django 4.0.4 on 2022-06-24 23:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_comment', models.TextField(blank=True, null=True)),
                ('evaluation', models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='system.doctor')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='system.patient')),
            ],
            options={
                'unique_together': {('owner', 'doctor')},
            },
        ),
    ]
