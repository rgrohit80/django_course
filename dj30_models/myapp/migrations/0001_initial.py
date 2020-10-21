# Generated by Django 3.1 on 2020-10-18 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('pagename', models.CharField(max_length=100)),
                ('pagecat', models.CharField(max_length=100)),
                ('pagedate', models.DateField()),
            ],
        ),
    ]
