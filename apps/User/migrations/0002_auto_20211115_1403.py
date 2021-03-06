# Generated by Django 3.2.9 on 2021-11-15 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('seconds_delivered_per_month', models.DecimalField(decimal_places=0, max_digits=15)),
                ('is_archived', models.SmallIntegerField(choices=[(0, 'Not archived'), (1, 'Archived')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.client'),
        ),
    ]
