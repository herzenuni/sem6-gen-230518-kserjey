import itertools

LIMIT = 10

def fib():
  a = 0
  b = 1
  
  while True:
    yield a
    b = a + b
    yield b
    a = a + b

series = fib()
print(list(itertools.islice(series, 10)))