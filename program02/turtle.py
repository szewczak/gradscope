import math

class Screen:
    def __init__(self):
        self.color = "white"

    def bgcolor(self, c):
        self.color = c

    def exitonclick(self):
        self.exit = True

class Turtle:
    """A mock version of turtle.py to allow grading 
    in non-graphics environment. """

    def color(self, *args):
        self.color = args

    def shape(self, sh):
        self.shape = sh

    def pensize(self,s):
        self.size += s

    def stamp(self):
        self.stamps += 1

    def __init__(self):
        self.heading = 0
        self.x = 0
        self.y = 0
        self.dist = 0
        self.turns = 0
        self.stamps = 0
        self.size = 1

    def left(self, angle):
        self.heading += int(angle) 
        self.turns += 1
        self.pr()
 

    def right(self, angle):
        self.heading -= int(angle) 
        self.turns += 1  
        self.pr()        

    def forward(self, d):
        self.dist += d
        hyp = math.sqrt(self.x*self.x + self.y*self.y)
        self.x += hyp * math.cos(math.radians(self.heading))
        self.y += hyp * math.sin(math.radians(self.heading))
        self.pr()
        
    def pr(self):
        s = "heading: " + str(self.heading%360) + " turns: " + str(self.turns)
        print(s)
