import pytest 
import os

def test_file2_method1():
	x=int(os.environ['x'])
	y=int(os.environ['y'])
	assert x+1 == y,"test failed"
	assert x == y,"test failed because x=" + str(x) + " y=" + str(y)

def test_file2_method2():
	x=int(os.environ['x'])
	y=int(os.environ['y'])
	assert x+1 == y,"test failed"
	