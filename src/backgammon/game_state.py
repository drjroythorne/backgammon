import numpy as np
from .board import Board

class GameState:

    def __init__(self):
        self.board = Board.start()
        self.current_player = 0
   
    def next_states(self, rolls):
        nxt = []
        board = self.board if self.current_player == 0 else self.board.invert()
        if rolls[0] == rolls[1]: #thrown a double
            permutations = [4*[rolls[0]]
        else:
            permutations = [rolls.copy(), list(reversed(rolls))]
        for r in permutations:
               nxt.extend(self._next_states(rolls=r, current_states=[(board, [])]))
        #must use both rolls if available, and must use biggest roll otherwise
        lengths, max_roll = zip(*[(len(x[1]), max(x[1])) for x in nxt])  
        max_length = max(lengths)
         
        allowed_states = [n for i, n in enumerate(nxt) if (lengths[i]==max_length) and (max_roll[i] == max(rolls))]
        return set(x[0] for x in allowed_states)
    
    def _next_states(self, rolls, current_states):
        nxt = []
        if not rolls:
            return current_states
        r = rolls.pop()
        for board, prv_rolls in current_states:
            b = board.bar
            p = board.points
            if b[0] > 0: #player has checkers on bar
                if p[1, r-1] == 0: 
                    new = board.copy()
                    new.bar[0] -= 1
                    new.points[0, r-1] +=1
                    nxt.append((new, prv_rolls + [r]))
                elif p[1, r-1] == 1: 
                    new = board.copy()
                    new.bar[0] -= 1
                    new.bar[1] += 1
                    new.points[:, r-1] = [1,0]
                    nxt.append((new, prv_rolls + [r]))
                else: #no move available
                    nxt.append((board.copy(), prv_rolls))
            else: #nothing on the bar
                for i in np.ravel(np.where(p[0,:]>0)):
                    t = i + r
                    if t > 23:
                        if board.can_bear_off():
                            if t == 24 or board.minpos() == i:
                                new = board.copy()
                                new.points[0, i] -= 1
                                nxt.append((new, prv_rolls + [r]))
                    else:
                        if p[1,t] == 0:
                            new = board.copy()
                            new.points[0, i] -= 1
                            new.points[0, t] += 1
                            nxt.append((new, prv_rolls + [r]))
                        elif p[1,t] == 1:
                            new = board.copy()
                            new.points[0, i] -= 1
                            new.points[:, t] += [1,0]
                            new.bar[1] += 1
                            nxt.append((new, prv_rolls + [r]))
                        else: #no move available
                            nxt.append((board.copy(), prv_rolls))
                        #print(nxt)
        #print(nxt)
        return self._next_states(rolls, nxt)
            
             
            
        
        


