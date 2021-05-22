from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, phone_no, city, password=None):

        if not email:
            raise ValueError("user must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone_no=phone_no, city=city)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_no, city, password):

        user = self.create_user(email, name, phone_no, city, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField(max_length=255, unique=True)
    name        = models.CharField(max_length=255, default='')
    phone_no    = models.CharField(max_length=20, default='')
    city        = models.CharField(max_length=50, default= 'New Delhi')

    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)

    objects     = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_no', 'city']

    def __str__(self):
        return self.name


class Ticket(models.Model):

    customer_name = models.CharField(default='Not Booked', max_length=100, blank=True)
    customer_phone = models.CharField(default='', max_length=15, blank=True)
    bought_on = models.DateTimeField(auto_now=True)
    game_id  = models.IntegerField()
    ticket_id = models.IntegerField()
    ticket = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.game_id} {self.ticket_id} - {self.customer_name}'
