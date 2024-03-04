# Generated by Django 2.2.6 on 2023-05-22 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_schooldata_by_professer_schooldata_by_professer_babies_schooldata_by_professer_close_schooldata_by_s'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_schools_by_year',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('년2016', models.FloatField()),
                ('년2017', models.FloatField()),
                ('년2018', models.FloatField()),
                ('년2019', models.FloatField()),
                ('년2020', models.FloatField()),
                ('년2021', models.FloatField()),
                ('년2022', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='all_students_by_year',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('년2010', models.FloatField()),
                ('년2011', models.FloatField()),
                ('년2012', models.FloatField()),
                ('년2013', models.FloatField()),
                ('년2014', models.FloatField()),
                ('년2015', models.FloatField()),
                ('년2016', models.FloatField()),
                ('년2017', models.FloatField()),
                ('년2018', models.FloatField()),
                ('년2019', models.FloatField()),
                ('년2020', models.FloatField()),
                ('년2021', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='schooldata_by_professer_close',
            name='학교명',
        ),
    ]
