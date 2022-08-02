from __future__ import print_function

import time

start = time.process_time()

map = {i: i for i in range(1, 2000001)}

sum = 0
for i in range(1, 2000001):
  sum = sum + map[i]
print(sum)

for i in range(1, 2000001):
  del map[i]

print(f"elapsed: {str(time.process_time() - start)}")