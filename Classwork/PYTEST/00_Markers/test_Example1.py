import pytest
import time

@pytest.mark.smoke_test
@pytest.mark.high
def test_file1_method1():
	x=5
	y=6
	time.sleep(3)
	assert x+1 == y,"First test failed"
	assert x == y, f"Second test failed"

@pytest.mark.high
def test_file1_method2():
	x=5
	y=6
	time.sleep(3)
	assert x+1 == y,"test failed"

@pytest.mark.medium
def test_file1_method3():
	time.sleep(3)
	assert True

@pytest.mark.medium
def test_file1_method4():
	time.sleep(3)
	assert False
