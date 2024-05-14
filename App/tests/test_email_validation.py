import pytest
from routes.main_routes import validate_email

emailRegex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

@pytest.mark.parametrize("email, expected_result", [
    ("user@example.com", True),
    ("user.name@example.com", True),
    ("user123@example.com", True),
    ("invalid_email", False),
    ("   ", False),
])
def test_validate_email(email, expected_result):
    # Act
    result = validate_email(email)

    # Assert
    assert result == expected_result

