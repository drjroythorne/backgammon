import sys
import numpy as np
from .game_state import GameState

def decide_start_player():
    #default to play 0 starts
    return 0

def roll():
    return list(np.random.randint(2, size=2))

def main(argv):
    state = GameState()
    state.current_player = decide_start_player()
    r = roll()
    nxt = state.next_states(r)




main(argv = sys.argv())
