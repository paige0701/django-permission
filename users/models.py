from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
from django.db import models
from django.db.models import Q
from django.utils import timezone

from users import permissions


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_active=True, **extra_fields):

        email = UserManager.normalize_email(email)

        user = self.model(email=email, is_active=is_active, is_staff=is_staff, **extra_fields)

        if password:
            user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, is_staff=True, is_superuser=True, **extra_fields)

    def normal_users(self):
        return self.get_queryset().filter(not permissions)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)

    date_joined = models.DateTimeField(default=timezone.now, editable=False)

    # admin 페이지 접근 가능
    is_staff = models.BooleanField(default=False)

    # 활성화 -> 유저는 삭제하지 않고 is_active를 false로 한다.
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        ordering = ('email',)
        permissions = (
            ('knowledge.view', 'View knowledge'),
            ('knowledge.create', 'Create knowledge'),
            ('knowledge.update', 'Update knowledge'),
            ('knowledge.delete', 'Delete knowledge'),
            ('user.view', 'View user'),
            ('user.create', 'Create user'),
            ('user.update', 'Update user'),
            ('user.delete', 'Delete user'),
            ('ontology.view', 'View ontology'),
            ('ontology.create', 'Create ontology'),
            ('ontology.update', 'Update ontology'),
            ('ontology.delete', 'Delete ontology'),
        )

    def __str__(self):
        return self.email