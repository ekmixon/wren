from __future__ import print_function

import time

# Map "range" to an efficient range in both Python 2 and 3.
try:
    range = xrange
except NameError:
    pass

start = time.process_time()
list = list(range(1000000))
sum = 0
for i in list:
  sum += i
print(sum)
print(f"elapsed: {str(time.process_time() - start)}")