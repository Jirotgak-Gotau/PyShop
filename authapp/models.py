from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.contrib.auth.models import User  # If you're using Django's built-in user model


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class CustomUser(Abstract, PermissionsMixin):
    username = models.CharField(unique=True, max_length=150)
    # Add other user fields as needed

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    # Add other required fields here

    def __str__(self):
        return self.username

    class Meta:
        permissions = (("can_view_special_content", "Can view special content"),)
        """groups = models.ManyToManyField(
            Group,
            verbose_name=_("groups"),
            blank=True,
            help_text=_(
                "The groups this user belongs to. A user will get all permissions granted to each of their groups."
            ),
            related_name="customuser_groups",
            related_query_name="customuser_group",
        )

        user_permissions = models.ManyToManyField(
            Permission,
            verbose_name=_("user permissions"),
            blank=True,
            help_text=_("Specific permissions for this user."),
            related_name="customuser_user_permissions",
            related_query_name="customuser_user_permission",
        )
        """
        
  