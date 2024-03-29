# Generated by Django 2.2.12 on 2021-05-20 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_delete_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('clave_nueva', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('documento', models.FileField(upload_to='documents/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.tipo_poliza')),
            ],
            options={
                'verbose_name': 'Dato',
                'verbose_name_plural': 'Datos',
            },
        ),
    ]
