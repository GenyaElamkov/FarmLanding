import pytest
from django.template import Template, Context
from django.core.files.uploadedfile import SimpleUploadedFile

from lending.models import (
    Hero,
    AboutFarm,
    Product,
    Gallery,
    About,
    Review,
    Contacts,
    SocialNetwork,
    Category,
)


@pytest.mark.django_db
class TestTemplateTags:
    @pytest.fixture
    def test_image(self):
        return SimpleUploadedFile(
            name="test_image.jpg",
            content=b"simple image content",
            content_type="image/jpeg",
        )

    def test_show_hero_tag(self, test_image):
        hero = Hero.objects.create(
            title="Тестовый заголовок",
            description="Тестовое описание",
            image=test_image,
        )

        template = Template("{% load lending_tags %} {% show_hero %}")
        context = Context({})
        rendered = template.render(context)

        assert hero.title in rendered
        assert hero.description in rendered

    def test_show_about_farm_tag(self):
        AboutFarm.objects.create(
            title="Тест 1",
            description="Описание 1",
            icon_class="fas fa-leaf",
        )
        AboutFarm.objects.create(
            title="Тест 2",
            description="Описание 2",
            icon_class="fas fa-egg",
        )

        template = Template("{% load lending_tags %} {% show_about_farm %}")
        context = Context({})
        rendered = template.render(context)

        assert "Тест 1" in rendered
        assert "Тест 2" in rendered
        assert "fas fa-leaf" in rendered
        assert "fas fa-egg" in rendered

    def test_show_all_products_tag(self, test_image):
        category = Category.objects.create(name="Овощи")
        product = Product.objects.create(
            name="Морковь",
            slug="carrot",
            description="Свежая морковь",
            category=category,
            featured=True,
            image=test_image,
        )

        template = Template("{% load lending_tags %} {% show_all_products %}")
        context = Context({})
        rendered = template.render(context)

        assert "Морковь" in rendered
        assert "Овощи" in rendered

    def test_show_all_gallery_tag(self, test_image):
        Gallery.objects.create(name="Тестовая галерея", image=test_image)

        template = Template("{% load lending_tags %} {% show_all_gallery %}")
        context = Context({})
        rendered = template.render(context)

        assert "Тестовая галерея" in rendered

    def test_show_about_tag(self, test_image):
        about = About.objects.create(
            title="О нас тест", description="Тестовое описание", image=test_image
        )

        template = Template("{% load lending_tags %} {% show_about %}")
        context = Context({})
        rendered = template.render(context)

        assert "О нас тест" in rendered
        assert "Тестовое описание" in rendered

    def test_show_reviews_tag(self, test_image):
        Review.objects.create(
            name="Иван Иванов",
            rating=5,
            description="Отличные продукты!",
            image=test_image,
        )

        template = Template("{% load lending_tags %} {% show_reviews %}")
        context = Context({})
        rendered = template.render(context)

        assert "Иван Иванов" in rendered
        assert "Отличные продукты!" in rendered

    def test_show_contacts_tag(self):
        contacts = Contacts.objects.create(
            address="Москва, ул. Тестовая", phone="+79123456789", email="test@test.ru"
        )

        template = Template("{% load lending_tags %} {% show_contacts %}")
        context = Context({})
        rendered = template.render(context)

        assert "Москва, ул. Тестовая" in rendered
        assert "test@test.ru" in rendered
