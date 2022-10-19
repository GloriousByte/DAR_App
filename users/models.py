from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=150, default='Orange Lake')
    Multiplier = models.CharField(max_length=150, default='Orange Lake')
    Due_date = models.CharField(max_length=150, default='Orange Lake')
    Month = models.CharField(max_length=150, default='Orange Lake')
    street = models.CharField(max_length=150, default='Orange Lake')
    house_number = models.CharField(max_length=150, default='77 Home A')
    amount_owed = models.CharField(max_length=150, default='1000gh')
    amount_owedtolls = models.CharField(max_length=150, default='1000gh')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    amount_due = models.DecimalField(max_digits=7, decimal_places=2, default='1000')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Bankaccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amountinaccount = models.DecimalField(max_digits=7, decimal_places=2)
    specialnumber = models.CharField(max_length=150, default='0000')
    lastthreedig = models.CharField(max_length=150, default='0000')

    class CreditCard(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        Account_Name = models.CharField(max_length=150, default='1000gh')
        Bank_UC = models.CharField(max_length=150, default='1000gh')
        Card_Number = models.CharField(max_length=150, default='0000')
        CUL = models.CharField(max_length=150, default='0000')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


class CreditCardTwo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Account_Name = models.CharField(max_length=150, default='1000gh')
    Bank_UC = models.CharField(max_length=150, default='1000gh')
    Card_Number = models.CharField(max_length=150, default='0000')
    CUL = models.CharField(max_length=150, default='0000')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class CreditCardPayments(models.Model):
    Account_Name = models.CharField(max_length=150, default='1000gh')
    Bank_UC = models.CharField(max_length=150, default='1000gh')
    Card_Number = models.CharField(max_length=150, default='0000')
    CUL = models.CharField(max_length=150, default='0000')
    Mail = models.CharField(max_length=150, default='Enter an email to receive receipt')
    Paymet_Comment = models.CharField(max_length=150, default='0000')
    signed_by = models.CharField(max_length=150, default='0000')
    payer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Account_Name

    def get_absolute_url(self):
        return reverse('creditcard-detail', kwargs={'pk': self.pk})


