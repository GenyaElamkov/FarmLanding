import os
import pytest
from phonenumber_field.phonenumber import PhoneNumber

from lending.models import (
    Category,
    Product,
    Gallery,
    About,
    Review,
    Hero,
    AboutFarm,
    Contacts,
    SocialNetwork,
)



def clean_up(file_path:str) -> None:
    """Удалеят тестовый файл"""
    if os.path.exists(file_path):
        os.remove(file_path)

@pytest.mark.django_db
class TestModels:
    def test_category_creation(self):
        category = Category.objects.create(name="Овощи")
        assert str(category) == "Овощи"
        assert category._meta.verbose_name == "Категория"
        assert category._meta.verbose_name_plural == "Категории"

    def test_product_creation(self, temp_media_root):
        category = Category.objects.create(name="Овощи")
        product = Product.objects.create(
            name="Морковь",
            slug="carrot",
            description="Свежая морковь",
            category=category,
            featured=True,
        )
        assert str(product) == "Морковь"
        assert product._meta.verbose_name == "Продукт"
        assert product._meta.verbose_name_plural == "Продукты"
        assert product.featured is True
        clean_up('src\media\products\test_image.jpg')

    def test_gallery_creation(self, temp_media_root):
        gallery = Gallery.objects.create(name="Ферма летом")
        assert str(gallery) == "Ферма летом"
        assert gallery._meta.verbose_name == "Галерея"
        assert gallery._meta.verbose_name_plural == "Галерея"


    def test_about_creation(self, temp_media_root):
        about = About.objects.create(
            title="О нашей ферме",
            description="Мы работаем с 2010 года",
        )
        assert str(about) == "О нашей ферме"
        assert about._meta.verbose_name == "О нас"
        assert about._meta.verbose_name_plural == "О нас"

    def test_review_creation(self, temp_media_root):
        review = Review.objects.create(
            name="Иван Иванов",
            rating=5,
            description="Отличные продукты!",
        )
        assert str(review) == "Иван Иванов"
        assert review._meta.verbose_name == "Отзыв"
        assert review._meta.verbose_name_plural == "Отзывы"
        assert review.rating == 5

    def test_hero_creation(self, temp_media_root):
        hero = Hero.objects.create(
            title="Эко Ферма Солнечная",
            description="Натуральные продукты",
        )
        assert str(hero) == "Эко Ферма Солнечная"
        assert hero._meta.verbose_name == "Гланый заголовок"
        assert hero._meta.verbose_name_plural == "Гланый заголовок"

    def test_about_farm_creation(self):
        about_farm = AboutFarm.objects.create(
            title="Наши ценности",
            description="Экологичность и качество",
            icon_class="fas fa-leaf",
        )
        assert str(about_farm) == "Наши ценности"
        assert about_farm._meta.verbose_name == "О ферме"
        assert about_farm._meta.verbose_name_plural == "О ферме"
        assert about_farm.icon_class == "fas fa-leaf"

    def test_contacts_creation(self):
        phone = PhoneNumber.from_string("+79123456789")
        contacts = Contacts.objects.create(
            address="Москва, ул. Ленина, 1",
            phone=phone,
            email="info@sunfarm.ru",
        )
        assert str(contacts) == "Москва, ул. Ленина, 1 / +79123456789 / info@sunfarm.ru"
        assert contacts._meta.verbose_name == "Контакт"
        assert contacts._meta.verbose_name_plural == "Контакты"

    def test_social_network_creation(self):
        social = SocialNetwork.objects.create(
            name="Telegram",
            base_url="https://t.me/sunfarm",
            icon_class="fab fa-telegram",
        )
        assert str(social) == "Telegram"
        assert social._meta.verbose_name == "Социальная сеть"
        assert social._meta.verbose_name_plural == "Социальные сети"
        assert social.icon_class == "fab fa-telegram"
