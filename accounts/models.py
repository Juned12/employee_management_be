from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular User with the given email and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class Manager(AbstractUser):
    """
    Custom User Model
    """

    email = models.EmailField(
        verbose_name='email address',
        max_length=128,
        unique=True
    )
    address = models.CharField(
        max_length=250,
        null=True
    )
    dob = models.DateField(
        max_length=8,
        null=True
    )
    company = models.CharField(
        max_length=128,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = UserManager()

    def __str__(self):           
        return self.email 

    def save(self, *args, **kwargs):
        self.username = self.email
        super(Manager, self).save(*args, **kwargs)

class Employee(models.Model):


    emp_id = models.CharField(
        max_length=10,
        verbose_name='Employee Id',
    )
    email = models.EmailField(
        max_length=250,
        verbose_name='Email address'
    )
    first_name = models.CharField(
        max_length=24,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        max_length=24,
        verbose_name='Last Name',
    )
    password = models.CharField(
        max_length=250
    )
    address = models.CharField(
        max_length=512,
    )
    dob = models.DateField(
        max_length=8,
        verbose_name='Date of Birth',
    )
    company = models.CharField(
        max_length=128
    )
    mobile = models.CharField(
        max_length=12
    )
    city = models.CharField(
        max_length=50
    )


