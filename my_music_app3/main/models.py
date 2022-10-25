from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from my_music_app3.main.validators import validate_if_username_contains_letters_numbers_and_underscores


class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 15

    username = models.CharField(max_length=MAX_LEN_USERNAME,
                                validators=(validate_if_username_contains_letters_numbers_and_underscores,
                                            MinLengthValidator(MIN_LEN_USERNAME))
                                )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    R_AND_B_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER = 'Other'

    CHOICES = [(x, x) for x in [POP_MUSIC, JAZZ_MUSIC, R_AND_B_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC,
                                HIP_HOP_MUSIC, OTHER]]

    MAX_LEN_ALBUM_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30
    MIN_PRICE = 0.0

    album_name = models.CharField(
        max_length=MAX_LEN_ALBUM_NAME,
        unique=True
    )

    artist = models.CharField(max_length=MAX_LEN_ARTIST)

    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        choices=CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )

''' 
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }),
        }
'''