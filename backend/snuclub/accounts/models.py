from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models

from core.fields import IntegerRangeField
from core.mixins import TimestampedMixin


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if username is None:
            raise TypeError('Users must have a username')

        if email is None:
            raise TypeError('Users must have an email address')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        # Todo Activate 이메일 전송 필요

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, TimestampedMixin):

    # 로그인시 사용되는 이메일 입니다.
    email = models.EmailField(db_index=True, unique=True)

    # 닉네임으로 사용되는 필드 입니다.
    username = models.CharField(max_length=10, unique=True)

    # 이메일 인증을 완료해야 계정이 활성화 됩니다.
    is_active = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    object = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 입학년도
    year_of_admission = IntegerRangeField(
        max_value=2500,
        min_value=1800,
        blank=True,
        null=True
    )

    # 학과정보
    department = models.CharField(max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(UserProfile, self).save(*args, **kwargs)
