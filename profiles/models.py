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


class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    game_is_live = models.BooleanField(default=False)
    drawn_numbers_list = models.CharField(default='', max_length=500)
    last_played_num = models.CharField(default='', max_length=100)
    last_played_winner = models.CharField(default='', max_length=100, blank=True)

    def __str__(self):
        return f'{self.game_id} - {self.start_time}'

class Ticket(models.Model):

    customer_name = models.CharField(default='Not Booked', max_length=100, blank=True)
    customer_phone = models.CharField(default='', max_length=15, blank=True)
    bought_on = models.DateTimeField(auto_now=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ticket', default='1')
    ticket_id = models.IntegerField()
    ticket = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.game_id} {self.ticket_id} - {self.customer_name}'

class Winner(models.Model):
    WINNER_TYPES = [
    ('TR', 'Top Row'),
    ('MR', 'Middle Row'),
    ('BR', 'Bottom Row'),
    ('Q5', 'Quick Five'),
    ('CO', 'Corners'),
    ('SR', 'Star'),
    ('HF', 'House Full'),
    ('SHF', 'Second House Full'),

]
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='winner')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='winner_game', default='1')
    win_type = models.CharField(max_length=3, choices=WINNER_TYPES, default='')

    def __str__(self):
        return f'{self.ticket} - {self.win_type}'
