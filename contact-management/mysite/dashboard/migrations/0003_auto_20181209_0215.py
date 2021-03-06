# Generated by Django 2.1.4 on 2018-12-08 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_complain'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoryRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=15)),
                ('employee_id', models.CharField(max_length=15)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AddAccessorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='accessoryrequest',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.AddAccessorie'),
        ),
    ]
