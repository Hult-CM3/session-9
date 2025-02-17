from calculator import multiply

def test_multiply():
    if multiply(2, 2) != 4:
            print("Test 1 failed")
    if multiply(4, 5) != 20:
            print("Test 2 failed") 














""" 
def test_multiply():
    try:
        assert multiply(2,2) == 4
    except:
        print("2 * 2 is not 4")         
"""





















""" 
def test_positive():
    assert multiply(2, 2) == 4
    assert multiply(4, 5) == 20

def test_negative():
    assert multiply(-2, -2) == 4
    assert multiply(-4, 5) == -20
    
def test_zero():
    assert multiply(0, 3) == 0
    assert multiply(0, -5) == 0 
"""