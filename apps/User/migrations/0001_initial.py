# Generated by Django 3.2.9 on 2021-11-15 02:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.SmallIntegerField(choices=[(1, 'General user'), (2, 'Host user')], default=0)),
                ('login_type', models.CharField(choices=[('email', 'EMAIL'), ('insta', 'INSTAGRAM'), ('facebook', 'FACEBOOK'), ('twitter', 'TWITTER')], default='email', max_length=45)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('remember_token', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_id', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_id', models.CharField(blank=True, max_length=255, null=True)),
                ('apple_id', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name_kanji', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name_kanji', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name_kana', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name_kana', models.CharField(blank=True, max_length=255, null=True)),
                ('nickname', models.CharField(max_length=255)),
                ('sex', models.SmallIntegerField(choices=[(0, 'Not known'), (1, 'Male'), (2, 'Female'), (9, 'Not applicable')], default=1)),
                ('is_sex_public', models.SmallIntegerField(choices=[(0, 'Private'), (1, 'Public')], default=1)),
                ('date_of_birth', models.DateField(auto_now_add=True)),
                ('is_date_of_birth_public', models.SmallIntegerField(choices=[(0, 'Private'), (1, 'Public')], default=1)),
                ('phone', models.CharField(blank=True, max_length=45, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=8, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('subsequent_address', models.CharField(blank=True, max_length=255, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('points_balance', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('points_reveived', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('stamps_balance', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('econtext_cus_id', models.CharField(blank=True, max_length=255, null=True)),
                ('delux_membership', models.CharField(blank=True, max_length=255, null=True)),
                ('host_user_type', models.SmallIntegerField(blank=True, choices=[(1, 'Individual'), (2, 'Group')], default=1, null=True)),
                ('isAuthenticated', models.SmallIntegerField(choices=[(0, 'Not authenticated'), (1, 'Authenticated'), (2, 'No authenticated required')], default=1, null=True)),
                ('is_archived', models.SmallIntegerField(choices=[(0, 'Not archived'), (1, 'Archived')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]