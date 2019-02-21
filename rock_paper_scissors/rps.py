#!/usr/bin/python

import sys

#This was the whiteboarding problem assigned to me as an interviewer
def rock_paper_scissors(n):
    outcomes = []
    plays = ["rock", "paper", "scissors"]
    def find_outcome(rounds, result=[]):
      if rounds == 0:
        outcomes.append(result)
        return
      for play in plays:
        find_outcome(rounds - 1, result + [play])
    find_outcome(n, [])
    return outcomes


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')