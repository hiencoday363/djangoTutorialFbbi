from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, PermissionsMixin

from apps.MasterData.models import Prefectures


class CustomAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        '''
        Create and save a user with the given email, and
        password.
        '''
        if not email:
            raise ValueError('The given email must be set')
            # timestamp = str(datetime.now().timestamp())
            # email = f"{timestamp}@admin.com"


        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        return self._create_user(email, password, **extra_fields)


# Create your models here.

class Client(models.Model):
    choice_archive = (
        (0, 'Not archived'),
        (1, 'Archived')
    )
    name = models.CharField(max_length=255)
    seconds_delivered_per_month = models.DecimalField(max_digits=15, decimal_places=0, null=False)
    is_archived = models.SmallIntegerField(null=False, choices=choice_archive, default=1)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return f'{self.name}'


class User(AbstractBaseUser, PermissionsMixin):
    AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                      'twitter': 'twitter', 'email': 'email'}
    choice_user = (
        (1, 'General user'),
        (2, 'Host user')
    )
    choice_login = (
        ('email', 'EMAIL'),
        ('insta', 'INSTAGRAM'),
        ('facebook', 'FACEBOOK'),
        ('twitter', 'TWITTER')
    )
    choice_sex = (
        (0, 'Not known'),
        (1, 'Male'),
        (2, 'Female'),
        (9, 'Not applicable')
    )
    choice_sex_public = (
        (0, 'Private'),
        (1, 'Public')
    )
    choice_user_type = (
        (1, 'Individual'),
        (2, 'Group')
    )
    choice_auth = (
        (0, 'Not authenticated'),
        (1, 'Authenticated'),
        (2, 'No authenticated required')
    )
    choice_archive = (
        (0, 'Not archived'),
        (1, 'Archived')
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    user_type = models.SmallIntegerField(null=False, default=0, choices=choice_user)
    login_type = models.CharField(max_length=45, null=False, default='email', choices=choice_login)
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)
    nickname = models.CharField(max_length=255, unique=True)
    remember_token = models.CharField(max_length=255, null=True, blank=True)
    facebook_id = models.CharField(max_length=255, null=True, blank=True)
    twitter_id = models.CharField(max_length=255, null=True, blank=True)
    apple_id = models.CharField(max_length=255, null=True, blank=True)
    last_name_kanji = models.CharField(max_length=255, null=True, blank=True)
    first_name_kanji = models.CharField(max_length=255, null=True, blank=True)
    last_name_kana = models.CharField(max_length=255, null=True, blank=True)
    first_name_kana = models.CharField(max_length=255, null=True, blank=True)

    sex = models.SmallIntegerField(null=False, choices=choice_sex, default=1)
    is_sex_public = models.SmallIntegerField(null=False, choices=choice_sex_public, default=1)
    date_of_birth = models.DateField(default=timezone.now)
    is_date_of_birth_public = models.SmallIntegerField(null=False, choices=choice_sex_public, default=1)
    phone = models.CharField(max_length=45, null=True, blank=True)
    zip_code = models.CharField(max_length=8, null=True, blank=True)
    prefecture_id = models.ForeignKey(Prefectures, max_length=11, on_delete=models.SET_NULL, null=True,
                                      blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    subsequent_address = models.CharField(max_length=255, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    points_balance = models.DecimalField(max_digits=15, decimal_places=0, null=True, blank=True)
    points_reveived = models.DecimalField(max_digits=15, decimal_places=0, null=True, blank=True)
    stamps_balance = models.DecimalField(max_digits=15, decimal_places=0, null=True, blank=True)
    econtext_cus_id = models.CharField(max_length=255, null=True, blank=True)
    delux_membership = models.CharField(max_length=255, null=True, blank=True)
    host_user_type = models.SmallIntegerField(null=True, choices=choice_user_type, default=1, blank=True)
    isAuthenticated = models.SmallIntegerField(null=True, default=1, choices=choice_auth)
    is_archived = models.SmallIntegerField(null=False, default=1, choices=choice_archive)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class Image_path(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    event_id = models.ForeignKey("Event.Events", on_delete=models.SET_NULL, null=True, related_name='img_path')
    box_notification_trans_content_id = models.ForeignKey("MasterData.Box_notification_trans_content",
                                                          on_delete=models.SET_NULL,
                                                          null=True, blank=True)
    file_name = models.CharField(max_length=255, null=False)
    dir_path = models.CharField(max_length=255, null=False)
    image_url = models.CharField(max_length=255)
    display_order = models.SmallIntegerField(null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def save(self, *args, **kwargs):
        # self.image_url = self.file_name + '/' + self.dir_path+"/"+self.image_url
        super(Image_path, self).save(*args, **kwargs)

    def __str__(self):
        return self.file_name


class Host_user_link(models.Model):
    id = models.AutoField(primary_key=True)
    host_user_id = models.ForeignKey("Livestream.Live_stream", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.TextField()
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.id


class User_additional_profile(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    additional_profile_item_id = models.ForeignKey('MasterData.Additional_profile_item', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.id


class Mgmt_portal_user(models.Model):
    choice_user_type = (
        (1, 'System admin user'),
        (2, 'Client user'),
        (3, 'Host user'))
    choice_archive = (
        (0, 'Not archived'),
        (1, 'Archived'))
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    user_type = models.IntegerField(choices=choice_user_type, default=1)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=255, null=True)
    is_archived = models.IntegerField(choices=choice_archive, default=1)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.id
