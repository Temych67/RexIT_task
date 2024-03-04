from django.db import models


class ClientCategory(models.Model):
    class GenderType(models.TextChoices):
        MALE = 'male', 'Чоловік'
        FEMALE = 'female', 'Жінка'

    category = models.CharField(max_length=255, blank=True, default='', help_text='Категорія')
    email = models.EmailField(max_length=255, blank=True, default='', help_text='Електронна пошта')
    first_name = models.CharField(max_length=100, default='', blank=True, help_text='Імʼя')
    last_name = models.CharField(max_length=100, default='', blank=True, help_text='Прізвище')
    birth_date = models.DateField(null=True, blank=True, help_text='Дата народження')
    gender = models.CharField(
        max_length=100,
        choices=GenderType.choices,
        default=GenderType.MALE,
        help_text='Стать',
    )

    class Meta:
        verbose_name = 'Категорія клієнта'
        verbose_name_plural = 'Категорії клієнта'
        ordering = ['-id']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'.strip()
