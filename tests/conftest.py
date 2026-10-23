import pytest

from src.student_manager import Student, StudentManager


@pytest.fixture
def valid_registration_data():
    return {
        "username": "alice_01",
        "email": "alice@example.com",
        "password": "Abcdef1!",
        "age": 25,
    }


@pytest.fixture
def sample_student():
    return Student(student_id="S001", name="Alice", email="alice@example.com")


@pytest.fixture
def empty_manager():
    return StudentManager()


@pytest.fixture
def populated_manager():
    manager = StudentManager()
    manager.add_student(Student(student_id="S001", name="Alice", email="alice@example.com"))
    manager.add_student(Student(student_id="S002", name="Bob", email="bob@example.com"))
    manager.add_student(Student(student_id="S003", name="Cara", email="cara@example.com"))
    manager.update_grade("S001", "MATH", 95)
    manager.update_grade("S002", "MATH", 85)
    manager.update_grade("S003", "MATH", 70)
    return manager
