import pytest
import sys

@pytest.mark.skip('no way of currently testing this')
def test_add_1():
	assert 100 + 200 == 400, "failed"

@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
def test_add_2():
	assert 100 + 200 == 300, "failed"

@pytest.mark.xfail
def test_add_3():
	assert 15 + 13 == 28, "failed"

@pytest.mark.xfail
def test_add_4():
	assert 15 + 13 == 100, "failed"

def test_add_5():
	assert 3 + 2 == 5, "failed"

def test_add_6():
	assert 3 + 2 == 6, "failed"