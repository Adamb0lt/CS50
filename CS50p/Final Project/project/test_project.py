import pytest
from unittest.mock import Mock, patch
from project import find1, find2, in_program  # Replace 'your_module' with the actual module name

@pytest.fixture
def mock_response():
    mock = Mock()
    mock.status_code = 200
    mock.json.return_value = {
        'current': {
            'temp_f': 75.0  # Replace with the desired temperature for your test
        }
    }
    return mock

@patch('project.requests.get')
def test_find1(mock_get, mock_response):
    # Configure the mock_get to return the mock_response
    mock_get.return_value = mock_response

    result = find1("New York")

    assert result == 75.0  # Replace with the expected temperature for your test

@patch('project.requests.get')
def test_find2(mock_get, mock_response):
    # Configure the mock_get to return the mock_response
    mock_get.return_value = mock_response

    result = find2("Los Angeles")

    assert result == 75.0  # Replace with the expected temperature for your test

@patch('builtins.input', return_value="New York")
@patch('project.requests.get')
def test_in_program(mock_get, mock_input, mock_response):
    # Configure the mock_get to return the mock_response
    mock_get.return_value = mock_response

    result = in_program(None)  # Pass None to avoid the input prompt

    assert result == "It is currently 75.0 degrees farenheit in New York"









