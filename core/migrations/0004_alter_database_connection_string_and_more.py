# Generated by Django 4.2.11 on 2024-06-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_historicaltemplate_database_template_database_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='connection_string',
            field=models.TextField(db_column='connection_string'),
        ),
        migrations.RenameField(
            model_name='database',
            old_name='connection_string',
            new_name='_connection_string',
        ),
        migrations.AlterField(
            model_name='database',
            name='backend',
            field=models.CharField(choices=[('MS', 'MSSQL'), ('PG', 'Postgres')], default='MS', max_length=2),
        ),
    ]
