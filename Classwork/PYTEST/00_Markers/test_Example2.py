import pytest
import time

@pytest.mark.high
def test_file2_method1():
	x=5
	y=6
	time.sleep(5)
	assert x+1 == y,"test failed"
	assert x == y,"test failed because x=" + str(x) + " y=" + str(y)

@pytest.mark.high
def test_file2_method2():
	x=5
	y=6
	time.sleep(5)
	assert x+1 == y,"test failed"
