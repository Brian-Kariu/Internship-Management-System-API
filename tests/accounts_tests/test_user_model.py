def test_user_filter(user):
    assert user.email == "test@mail.com"


def test_user_update(user):
    user.role = "lecturer"
    user.save()
    assert user.role == "lecturer"
