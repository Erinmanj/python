# Generated by Django 5.0.6 on 2024-05-28 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('image', models.TextField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'bill',
            },
        ),
        migrations.CreateModel(
            name='DetailsofPatient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255, null=True)),
                ('middlename', models.CharField(max_length=255, null=True)),
                ('lastname', models.CharField(max_length=255, null=True)),
                ('gender', models.CharField(max_length=255, null=True)),
                ('dob', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('maritalst', models.CharField(max_length=255, null=True)),
                ('maidenname', models.CharField(max_length=255, null=True)),
                ('flatno', models.BigIntegerField(null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('ct', models.CharField(max_length=255, null=True)),
                ('otherlocality', models.CharField(max_length=255, null=True)),
                ('pin', models.BigIntegerField(null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('locality', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('tele', models.BigIntegerField(null=True)),
                ('mobile', models.BigIntegerField(null=True)),
            ],
            options={
                'db_table': 'DetailsofPatient',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone_no', models.BigIntegerField()),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Reciept',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('image', models.TextField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'reciept',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('image', models.TextField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'report',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'speciality',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('image', models.TextField(blank=True, max_length=50, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='hospitalapp.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='hospitalapp.detailsofpatient')),
                ('speciality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='hospitalapp.speciality')),
            ],
            options={
                'db_table': 'prescription',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='hospitalapp.speciality'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.TimeField(null=True)),
                ('date', models.DateField(null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='hospitalapp.detailsofpatient')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='hospitalapp.doctor')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='hospitalapp.speciality')),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
    ]
