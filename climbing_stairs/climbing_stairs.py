#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  if cache is None: cache = [0] * (n + 1)

  if cache[n] > 0:
    return cache[n]

  if (n == 1 or n == 0):
    cache[n] = 1
    return 1
  elif (n == 2):
    cache[n] = 2
    return 2
  else:
    cache[n] = climbing_stairs(n - 3, cache) + climbing_stairs(n - 2, cache) + climbing_stairs(n - 1, cache)
    return cache[n]

print(climbing_stairs(0))
print(climbing_stairs(1))
print(climbing_stairs(2))
print(climbing_stairs(5))
print(climbing_stairs(10))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')