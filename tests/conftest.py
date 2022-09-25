import pytest

import main

@pytest.fixture(scope='module')
def schema():
    return main.schema