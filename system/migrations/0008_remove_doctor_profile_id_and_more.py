# Generated by Django 4.0.4 on 2022-06-24 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_alter_profile_type_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='profile_id',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='patientDoctor',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='profile_id',
        ),
        migrations.RemoveField(
            model_name='patient_chronic_diseases',
            name='chronic_diseases_id',
        ),
        migrations.RemoveField(
            model_name='patient_chronic_diseases',
            name='patient_id',
        ),
        migrations.RemoveField(
            model_name='pregnant_patient',
            name='patient_id',
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='review',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='review',
            name='owner',
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='type_id',
        ),
        migrations.AddField(
            model_name='profile',
            name='type_name',
            field=models.CharField(blank=True, choices=[('doctor', 'doctor'), ('patient', 'patient')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='ChestDetails',
        ),
        migrations.DeleteModel(
            name='Chronic_diseases',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Patient_chronic_diseases',
        ),
        migrations.DeleteModel(
            name='Pregnant_patient',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
