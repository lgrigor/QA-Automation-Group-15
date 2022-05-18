import pytest 

def test_first_compare(supply_list, supply_data):
	assert supply_list[0] == supply_data, "First comparison failed"

def test_second_compare(supply_list, supply_data):
	assert supply_list[1] == supply_data, "Second comparison failed"

def test_third_compare(supply_list, supply_data):
	assert supply_list[2] == supply_data, "Third comparison failed"