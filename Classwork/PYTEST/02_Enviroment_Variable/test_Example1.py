import pytest 
import os

def test_file1_method1():
	x=int(os.environ['x'])
	y=int(os.environ['y'])
	assert x+1 == y,"First test failed"
	assert x == y, f"Second test failed"

def test_file1_method2():
	x=int(os.environ['x'])
	y=int(os.environ['y'])
	assert x+1 == y,"test failed"

def test_file1_method3():
	assert True

def test_file1_method4():
	assert False
