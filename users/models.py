from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.db import models


# Create your models here.
class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    ]

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = [
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    ]

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = [
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    ]

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, blank=True, max_length=2, default=LANGUAGE_ENGLISH
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, blank=True, max_length=3, default=CURRENCY_USD
    )
    superhost = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
