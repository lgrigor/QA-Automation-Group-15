import pytest

@pytest.fixture
def supply_list():
	return [25, 35, 45]

@pytest.fixture
def supply_data():
    return 35