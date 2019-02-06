import math

class Screen:
    def __init__(self):
        self.col = "white"

    def bgcolor(self, c):
        self.col = c
        self.pr()

    def exitonclick(self):
        self.exit = True

    def pr(self):
        s = "bgcolor: " + self.col
        print(s)

class Turtle:
    """A mock version of turtle.py to allow grading 
    in non-graphics environment. """

    def color(self, c):
         self.col = c
         self.pr()

#    def color(self, *args):
#        self.col = args

    def shape(self, sh):
        self.shape = sh

    def __init__(self):
        self.heading = 0
        self.x = 0
        self.y = 0
        self.dist = 0
        self.turns = 0
        self.size = 1
        self.col = "black"
        self.size = 1
        #self.pr()

    def left(self, angle):
        self.heading += int(angle) 
        self.turns += 1
        #self.pr()
 

    def right(self, angle):
        self.heading -= int(angle) 
        self.turns += 1  
        #self.pr()        

    def forward(self, d):
        self.dist += d
        hyp = math.sqrt(self.x*self.x + self.y*self.y)
        self.x += hyp * math.cos(math.radians(self.heading))
        self.y += hyp * math.sin(math.radians(self.heading))
        #self.pr()

    def pensize(self, s):
        self.size = s
        #self.pr()
    
    
    def pr(self):
        #s = "heading: " + str(self.heading%360) + " turns: " + str(self.turns) + " size: " + str(self.size)
        s = "color: " + self.col
        print(s)
