from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.text import slugify


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username or password is None:
            raise ValueError('Required.')

        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if not username or password is None:
            raise ValueError('Required.')

        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True

        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)

        user.set_password(password)
        user.save()

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Логин", max_length=50, unique=True)
    # email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=12, verbose_name='Имя', null=True)
    last_name = models.CharField(max_length=12, verbose_name='Фамилия', null=True)
    is_active = models.BooleanField(default=True, verbose_name='Прошел активацию')
    is_staff = models.BooleanField(default=False, verbose_name='Служебный аккаунт')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def has_perm(*args, **kwargs):
        return True

    def has_module_perms(*args, **kwargs):
        return True

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']


"""Модель Категория"""
class Category(models.Model):
    name = models.CharField("Наименование", max_length=255)

    CATEGORY_TYPE_CHOICES = (
        ("ОБЯЗАТЕЛЬНАЯ", "обязательная"),
        ("НЕОБЯЗАТЕЛЬНАЯ", "необязательная"),
    )

    category_type = models.CharField("Тип категории", max_length=255, choices=CATEGORY_TYPE_CHOICES, default="ОБЯЗАТЕЛЬНАЯ")

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


"""Модель Доход"""
class Revenue(models.Model):
    sum = models.DecimalField("Сумма", max_digits=10, decimal_places=2)

    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)

    revenue_date = models.DateField("Дата получения")

    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + " " + str(self.category) + " " + str(self.sum)

    class Meta:
        verbose_name = "Доход"
        verbose_name_plural = "Доходы"


"""Модель Расход"""
class Expenditure(models.Model):
    sum = models.DecimalField("Сумма", max_digits=10, decimal_places=2)

    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)

    EXPENDITURE_TYPE_CHOICES = (
        ("КАРТА", "карта"),
        ("НАЛИЧНЫЕ", "наличные"),
    )

    expenditure_type = models.CharField("Тип расхода", max_length=255, choices=EXPENDITURE_TYPE_CHOICES, default="КАРТА")

    expenditure_date = models.DateField("Дата расхода")

    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE, null=True)

    comment = models.TextField("Комментарий", null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + " " + str(self.category) + " " + str(self.sum)

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"
