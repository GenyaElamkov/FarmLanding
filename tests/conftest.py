# conftest.py
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.fixture
def test_image():
    return SimpleUploadedFile(
        name='test_image.jpg',
        content=b'simple image content',
        content_type='image/jpeg'
    )