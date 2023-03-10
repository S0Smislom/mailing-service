# Generated by Django 4.1.5 on 2023-01-07 16:43

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('operator_code', models.CharField(max_length=12)),
                ('tag', models.CharField(max_length=32)),
                ('timezone', timezone_field.fields.TimeZoneField(choices_display='WITH_GMT_OFFSET')),
            ],
        ),
    ]
