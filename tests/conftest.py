import pytest

from fastapi.testclient import TestClient
from main import schema

from main import app

@pytest.fixture(scope='module')
def test_app():
    return schema