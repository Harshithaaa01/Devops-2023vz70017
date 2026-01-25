import calculator

def test_add():
 assert calculator.add(2, 3) == 5


def test_subtract():
 assert calculator.subtract(5, 3) == 2


def test_multiply():
 assert calculator.multiply(3, 4) == 12


def test_divide():
 assert calculator.divide(6, 3) == 2