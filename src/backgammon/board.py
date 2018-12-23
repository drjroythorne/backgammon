import numpy as np
class Board:
        
    def __init__(self, points, bar):
        self.points = points
        self.bar = bar

    @classmethod
    def start(cls):
        p = np.zeros((2,24), dtype=np.uint8) 
        p[0,0], p[0,11], p[0,16], p[0,18] = 2, 5, 3, 5
        p[1,23], p[1,12], p[1,7], p[1,5] = 2, 5, 3, 5
        bar = np.zeros((2,1), dtype=np.uint8)
        return cls(points = p, bar = bar)

    def __repr__(self):
        return 'points: {}, bar: {}'.format(self.points, self.bar)

    def __hash__(self):
        return hash((hash(self.points.data.tobytes()), hash(self.bar.data.tobytes())))

    def copy(self):
        return Board(points = np.copy(self.points), bar = np.copy(self.bar))

    def invert(self):
        return Board(points = np.flip(self.points), bar = np.flip(self.bar))

    def can_bear_off(self):
        return (np.min(np.where(self.points[0,:] == 0)) >= 18) and self.bar[0] == 0

