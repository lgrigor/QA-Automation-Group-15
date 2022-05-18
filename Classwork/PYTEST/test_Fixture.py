import pytest

@pytest.fixture
def supply_list():
	return [25, 35, 45]

@pytest.fixture
def supply_data():
    return 35

def test_first_compare(supply_list, supply_data):
	assert supply_list[0] == supply_data, "First comparison failed"

def test_second_compare(supply_list, supply_data):
	assert supply_list[1] == supply_data, "Second comparison failed"

def test_third_compare(supply_list, supply_data):
	assert supply_list[2] == supply_data, "Third comparison failed"