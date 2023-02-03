#from kpr import main
#from kpr.main import func
from kpr.lib.helper import helper_func

def test_kpr():
    assert 1 == 1

#def test_func():
#    assert func() == "Hello from func"

def test_h():
    assert helper_func() == "Hello from helper"