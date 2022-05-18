import pytest
import time

def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"First test failed"
	assert x == y, f"Second test failed"

def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed"

def test_file1_method3():
	assert True

def test_file1_method4():
	assert False