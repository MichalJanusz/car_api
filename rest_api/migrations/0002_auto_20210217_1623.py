# Generated by Django 3.1.6 on 2021-02-17 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='rate',
            new_name='rating',
        ),
        migrations.AlterField(
            model_name='rate',
            name='car_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='rest_api.car'),
        ),
    ]
