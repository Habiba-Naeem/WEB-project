from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
#from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'customer'),
        (2, 'seller'),
        (3, 'deliverer'),
        (4, 'admin'),
    )
    username = None
    user_type = models.PositiveSmallIntegerField(choices = USER_TYPE_CHOICES)
    email = models.EmailField(_('email address'), unique=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
 


class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name="seller")
    name = models.CharField(max_length=100)
    address = models.CharField(max_length = 50)
    contact = models.PositiveIntegerField(default=123)
    homeornot = models.BooleanField(default=False)
    #homeornot = models.CharField(max_length=1, default='Y')
    avg_rating = models.FloatField(default=0)
    category = models.CharField(max_length=100, default='Fast food')
    
    def __str__(self):
        return f"{self.user}, {self.name}, {self.address}, {self.contact}"

class Deliverer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length = 20)
    phone_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.user}, {self.name}, {self.vehicle_number}, {self.phone_number}"