from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    """Описание категории"""

    name = models.CharField(max_length=50, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """Описания продукта"""

    name = models.CharField(max_length=100, verbose_name="Имя продукта")
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, verbose_name="Описания продукта")
    image = models.ImageField(upload_to="products")
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="category_product",
        verbose_name="Категория",
    )
    featured = models.BooleanField(verbose_name="Наличие")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self) -> str:
        return self.name


class Gallery(models.Model):
    """Картинки для Галереи"""

    name = models.CharField(max_length=50, verbose_name="Имя картинки")
    image = models.ImageField(upload_to="gallery")

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"

    def __str__(self) -> str:
        return self.name


class About(models.Model):
    """Описание о нас"""

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    """Отызывы"""

    image = models.ImageField(upload_to="review")
    name = models.CharField(max_length=150, verbose_name="ФИО")
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0,
        verbose_name="Оценка",
    )
    description = models.TextField(max_length=500, blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self) -> str:
        return self.name


class Hero(models.Model):
    """Секция hero"""

    title = models.CharField(max_length=250, verbose_name="Заголовок")
    description = models.TextField(max_length=500, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="hero")

    class Meta:
        verbose_name = "Гланый заголовок"
        verbose_name_plural = "Гланый заголовок"

    def __str__(self) -> str:
        return self.title


class AboutFarm(models.Model):
    "Секция о ферме"
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    description = models.TextField(max_length=500, blank=True, verbose_name="Описание")
    icon_class = models.CharField(
        max_length=50,
        verbose_name="Класс иконки",
        choices=[
            ("fas fa-egg", "Яйцо"),
            ("fas fa-kiwi-bird", "Перепёлка"),
            ("fas fa-crow", "Курица (стилизовано)"),
            ("fas fa-feather", "Птицеводство"),
            ("fas fa-carrot", "Овощи"),
            ("fas fa-apple-alt", "Фрукты"),
            ("fas fa-cheese", "Молочные продукты"),
            ("fas fa-seedling", "Зелень"),
            ("fas fa-wheat", "Зерновые"),
            ("fas fa-cow", "Мясо"),
            ("fas fa-leaf", "Экология"),
            ("fas fa-tractor", "Техника"),
            ("fas fa-hands", "Ручная работа"),
        ],
        default="fas fa-leaf",
    )

    class Meta:
        verbose_name = "О ферме"
        verbose_name_plural = "О ферме"

    def __str__(self) -> str:
        return self.title


class Contacts(models.Model):
    """Описания контактов"""

    address = models.CharField(max_length=150, verbose_name="Адрес")
    phone = PhoneNumberField(region="RU", verbose_name="Контактный телефон")
    email = models.EmailField(verbose_name="Электронная почта")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self) -> str:
        return f"{self.address} / {self.phone} / {self.email}"


class SocialNetwork(models.Model):
    "Описания социальных сетей"

    name = models.CharField(max_length=50)
    base_url = models.URLField()
    icon_class = models.CharField(
        max_length=50,
        verbose_name="Класс иконки",
        choices=[
            ("fab fa-vk", "VK"),
            ("fab fa-telegram", "Telegram"),
            ("fab fa-whatsapp", "WhatsApp"),
            ("fab fa-instagram", "Instagram"),
            ("fab fa-youtube", "YouTube"),
        ],
        default="fab fa-telegram",
    )

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return self.name
