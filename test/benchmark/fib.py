from __future__ import print_function

import time

def fib(n):
  return n if n < 2 else fib(n - 1) + fib(n - 2)

start = time.process_time()
for _ in range(5):
  print(fib(28))
print(f"elapsed: {str(time.process_time() - start)}")