class Board:
    
    class Point:
        self.whites = 0
        self.reds = 0
        
        def __call__(self, whites, reds):
            self.whites = whites
            self.reds = reds
        
    def __init__(self):
        self.points = 24*[Point()] #points ordered from white's home board to red's home board
        self.init_checkers()
    
    def init_checkers(self):
        p = self.points #for brevity
        p[0](0,2)
        p[6](5,0)
        p[8](3,0)
        p[12](0,5)
        p[13](5,0)
        p[17](0,3)
        p[19](0,5)
        p[24](2,0)
    
    def draw(self):
        
    