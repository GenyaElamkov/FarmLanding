import pytest
import tempfile
import shutil
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings


@pytest.fixture(scope="session")
def temp_media_root():
    """Создает временную MEDIA_ROOT для всех тестов."""
    # Создаем временную директорию
    temp_dir = tempfile.mkdtemp()

    # Сохраняем оригинальный MEDIA_ROOT
    original_media_root = settings.MEDIA_ROOT

    # Устанавливаем временный MEDIA_ROOT
    settings.MEDIA_ROOT = temp_dir

    # Создаем поддиректории, которые могут понадобиться
    os.makedirs(os.path.join(temp_dir, 'products'), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, 'gallery'), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, 'about'), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, 'review'), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, 'hero'), exist_ok=True)

    yield temp_dir

    # Удаляем временную директорию после всех тестов
    shutil.rmtree(temp_dir)

    # Восстанавливаем оригинальный MEDIA_ROOT
    settings.MEDIA_ROOT = original_media_root


@pytest.fixture
def test_image():
    """Фикстура для создания тестового изображения."""
    return SimpleUploadedFile(
        name="test_image.jpg",
        content=b"simple image content",
        content_type="image/jpeg",
    )