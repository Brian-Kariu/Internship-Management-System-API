import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def user(db):
    instance = User.objects.create(
        email="test@mail.com", date_of_birth='2006-10-25',
        role='student', password='password1')
    return instance
