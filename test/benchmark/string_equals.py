from __future__ import print_function

import time
start = time.process_time()

count = 0
for _ in range(1000000):
  count = count + 1
  count = count + 1
  count = count + 1

  if "" == "abc":
    count = count + 1
  if "abc" == "abcd":
    count = count + 1
  if "changed one character" == "changed !ne character":
    count = count + 1
  if "123" == 123: count = count + 1
  if "a slightly longer string" == \
     "a slightly longer string!":
      count = count + 1
  if "a slightly longer string" == \
     "a slightly longer strinh":
      count = count + 1
  if "a significantly longer string but still not overwhelmingly long string" == \
     "another":
      count = count + 1

print(count)
print(f"elapsed: {str(time.process_time() - start)}")
