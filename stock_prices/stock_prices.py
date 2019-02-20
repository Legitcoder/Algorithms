#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maximum = max(prices)
  minimum = min(prices)

  remaining_max = 0

  while prices.index(maximum) < prices.index(minimum):
    prices.remove(maximum)
    maximum = max(prices)
    if prices.index(minimum) + 1 < len(prices):
      prices.remove(minimum)
      minimum = min(prices)
    if len(prices) == 2: remaining_max = maximum

  net = maximum - minimum
  print(net)
  if net == 0: return -(remaining_max - minimum)

  return net


find_max_profit([10, 7, 5, 8, 11, 9])
find_max_profit([100, 90, 80, 50, 20, 10])
find_max_profit([1050, 270, 1540, 3800, 2])
find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79])


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))