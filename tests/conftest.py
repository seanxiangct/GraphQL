import pytest

from main import schema

@pytest.fixture(scope='module')
def test_app():
    return schema