a = int(input())
b = int(input())
l1 = [int(x) for x in input().split()]


ROCK = 0
SCISSORS = 2
PAPER = 5
WINNING_PLAY_VS = {ROCK: PAPER,
                   PAPER: SCISSORS,
                   SCISSORS: ROCK}


#for i in range(b):
   # if 