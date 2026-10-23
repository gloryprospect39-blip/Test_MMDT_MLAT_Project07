import pytest

from src.data_validator import (
    InvalidAgeError,
    InvalidEmailError,
    InvalidUsernameError,
    ValidationError,
    WeakPasswordError,
    validate_age,
    validate_email,
    validate_password,
    validate_registration,
    validate_username,
)


@pytest.mark.parametrize(
    "email",
    [
        "user@example.com",
        "first.last+tag@sub.example.org",
        "user_name-123@domain.co.uk",
    ],
)
def test_validate_email_valid(email):
    assert validate_email(email) is True


@pytest.mark.parametrize(
    "email",
    [
        "",
        "user@domain",
        "user@@example.com",
        "user name@example.com",
        "user..name@example.com",
        "user@example",
    ],
)
def test_validate_email_invalid(email):
    with pytest.raises(InvalidEmailError):
        validate_email(email)


def test_validate_email_rejects_non_string():
    with pytest.raises(TypeError):
        validate_email(123)


@pytest.mark.parametrize(
    "password",
    [
        "Abcdef1!",
        "StrongPass9@",
        "B3tter!mypass",
    ],
)
def test_validate_password_valid(password):
    assert validate_password(password) is True


@pytest.mark.parametrize(
    "password",
    [
        "short1!",
        "alllowercase1!",
        "ALLUPPERCASE1!",
        "NoDigitHere!",
        "NoSpecialChar1",
        "Has space1!",
    ],
)
def test_validate_password_invalid(password):
    with pytest.raises(WeakPasswordError):
        validate_password(password)


def test_validate_password_rejects_non_string():
    with pytest.raises(TypeError):
        validate_password(None)


@pytest.mark.parametrize(
    "username",
    [
        "ab1",
        "user_name",
        "validUsername_99",
    ],
)
def test_validate_username_valid(username):
    assert validate_username(username) is True


@pytest.mark.parametrize(
    "username",
    [
        "ab",
        "a b",
        "@user",
        "user!name",
        "a" * 21,
    ],
)
def test_validate_username_invalid(username):
    with pytest.raises(InvalidUsernameError):
        validate_username(username)


def test_validate_username_rejects_non_string():
    with pytest.raises(TypeError):
        validate_username(123)


@pytest.mark.parametrize(
    "age",
    [13, 18, 25, 120],
)
def test_validate_age_valid(age):
    assert validate_age(age) is True


@pytest.mark.parametrize(
    "age",
    [12, 0, -5, 121],
)
def test_validate_age_invalid(age):
    with pytest.raises(InvalidAgeError):
        validate_age(age)


def test_validate_age_rejects_invalid_types():
    with pytest.raises(TypeError):
        validate_age(True)

    with pytest.raises(TypeError):
        validate_age("25")


def test_validate_registration_valid(valid_registration_data):
    assert validate_registration(valid_registration_data) is True


def test_validate_registration_missing_required_field(valid_registration_data):
    invalid_data = valid_registration_data.copy()
    invalid_data.pop("password")
    with pytest.raises(ValidationError, match="password"):
        validate_registration(invalid_data)


def test_validate_registration_rejects_non_dict():
    with pytest.raises(TypeError):
        validate_registration(["not", "a", "dict"])
