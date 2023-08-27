from calculator import Add, Subtract, Multiply, Divide

def test_addition():
    op = Add(5, 3)
    op.perform_operation()
    assert op.result == 8

def test_subtraction():
    op = Subtract(10, 4)
    op.perform_operation()
    assert op.result == 6

def test_multiplication():
    op = Multiply(7, 2)
    op.perform_operation()
    assert op.result == 14

def test_division():
    op = Divide(15, 3)
    op.perform_operation()
    assert op.result == 5
