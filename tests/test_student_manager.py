import pytest

from src.student_manager import Student, StudentManager


@pytest.mark.parametrize(
    "student_id, name, email, expected",
    [
        ("S001", "Alice", "alice@example.com", True),
        ("S002", "Bob", "bob@example.com", True),
    ],
)
def test_student_valid(student_id, name, email, expected):
    student = Student(student_id=student_id, name=name, email=email)
    assert isinstance(student, Student)
    assert student.student_id == student_id
    assert student.name == name
    assert student.email == email
    assert student.grades == {}
    assert expected is True


@pytest.mark.parametrize(
    "student_id, name, email",
    [
        ("", "Alice", "alice@example.com"),
        ("S001", "", "alice@example.com"),
        ("S001", "Alice", ""),
        ("S001", "Alice", "not-an-email"),
    ],
)
def test_student_invalid_values(student_id, name, email):
    with pytest.raises(ValueError):
        Student(student_id=student_id, name=name, email=email)


def test_student_add_grade_updates_and_rejects_bad_values(sample_student):
    sample_student.add_grade("MATH", 90)
    assert sample_student.grades["MATH"] == 90.0

    sample_student.add_grade("SCIENCE", 88.5)
    assert sample_student.grades["SCIENCE"] == 88.5

    with pytest.raises(ValueError):
        sample_student.add_grade("CHEM", 101)

    with pytest.raises(TypeError):
        sample_student.add_grade("CHEM", True)


def test_student_get_gpa(sample_student):
    sample_student.add_grade("MATH", 95)
    sample_student.add_grade("SCI", 85)
    sample_student.add_grade("ENG", 75)
    sample_student.add_grade("BIO", 55)

    assert sample_student.get_gpa() == 2.25

    blank_student = Student(student_id="S002", name="Bob", email="bob@example.com")
    assert blank_student.get_gpa() == 0.0


def test_manager_add_student_and_lookup(empty_manager):
    student = empty_manager.add_student("S001", "Alice", "alice@example.com")
    assert empty_manager.get_total_students() == 1
    assert empty_manager.get_student("S001") is student
    assert empty_manager.get_all_students() == [student]


def test_manager_duplicate_student_id_raises_value_error(empty_manager):
    empty_manager.add_student("S001", "Alice", "alice@example.com")
    with pytest.raises(ValueError, match="already exists"):
        empty_manager.add_student("S001", "Duplicate", "dup@example.com")


def test_manager_add_student_object(empty_manager):
    student = Student(student_id="S002", name="Bob", email="bob@example.com")
    added = empty_manager.add_student(student)
    assert added is student
    assert empty_manager.get_student("S002") is student


def test_manager_update_grade_returns_gpa(empty_manager):
    empty_manager.add_student("S001", "Alice", "alice@example.com")
    assert empty_manager.update_grade("S001", "MATH", 97) == 4.0
    assert empty_manager.calculate_gpa("S001") == 4.0


def test_manager_remove_student(empty_manager):
    empty_manager.add_student("S001", "Alice", "alice@example.com")
    assert empty_manager.remove_student("S001") is True
    assert empty_manager.get_total_students() == 0

    with pytest.raises(KeyError):
        empty_manager.remove_student("S999")


def test_manager_get_top_performers(populated_manager):
    top_students = populated_manager.get_top_performers(2)
    assert [student.student_id for student in top_students] == ["S001", "S002"]

    with pytest.raises(ValueError):
        populated_manager.get_top_performers(0)


def test_manager_filter_by_min_gpa(populated_manager):
    filtered = populated_manager.filter_by_min_gpa(3.0)
    assert [student.student_id for student in filtered] == ["S001", "S002"]

    with pytest.raises(ValueError):
        populated_manager.filter_by_min_gpa(-1)

    with pytest.raises(ValueError):
        populated_manager.filter_by_min_gpa(5)
