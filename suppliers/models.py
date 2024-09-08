from django.db import models
from django.utils import timezone


NULLABLE = {"blank": True, "null": True}

class Supplier(models.Model):
    """Модель звена торговой сети электроники."""

    LINK_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=150, verbose_name='Наименование')
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Номер дома')
    link = models.IntegerField(choices=LINK_CHOICES, verbose_name='Иерархическая структура сети')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Поставщик', related_name='suppliers')
    debit_arrears = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Дебиторская задолженность')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Время создания')

    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, **NULLABLE, verbose_name="Владелец звена сети", help_text="Укажите владельца звена сети")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'
