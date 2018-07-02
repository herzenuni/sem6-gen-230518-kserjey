from itertools import islice
from fibonacci import fib

def test_fib():
  series = fib()
  expected = [0, 1, 1, 2, 3, 5]
  assert list(islice(series, 6)) == expected