
class Stjerne:
    def __init__(self):
        self.farvex = 0
        self.x = random(0, 1920)
        self.y = random(0, 1080)
        self.color = color(255,250,232, 0)
        self.tilstand = random(0,200)
        self.c = 255
        
    def farve(self):
        
        
        if random(0,100) <= 1:
            self.tilstand = 1
            print("start")
            
    def tick(self):
        if self.tilstand == 1:
            self.c -= 1
            self.color = color(255,250,232,self.c)
            if self.c <= 0:
                self.tilstand = 2
        if self.tilstand == 2:
            self.c += 1
            self.color = color(255,250,232,self.c)
            if self. c > 255:
                self.tilstand = 0
        fill(self.color)
        circle(self.x, self.y, 5)
