from fibonachi import Fibonachi

def test_fibo():
    fib = Fibonachi()
    res = fib.calculate_nth(4)
    assert res == 3
