from Effekter import Stjerne


def setup():
    global photo, effekter, photostation, photorocket, photonout, photobench
    fullScreen()
    size(1920,1080)
    photo = loadImage("Timeline.png")
    effekter = [Stjerne() for i in range(1000)]
    photostation = loadImage("SpaceStation.jpg")
    photorocket = loadImage("Rocket.png")
    photonout = loadImage("Astronout.png")
    photobench = loadImage("Bench.jpg")
    
def slide(tilstand):
    global x, photo, photostation, photorocket, photonout, photobench
    
    if tilstand == "hub":
        fill(255,0,0)
        rect(0,0,200,200)
        scale(0.2)
        image(photostation, 2400, 200)
        scale(0.3)
        image(photorocket, -1000,-1000)
        scale(10)
        rotate(320)
        image(photonout, 2100,1150)
        scale(0.5)
        image(photobench, 3200, 4400)
        
    elif tilstand == "timeline":
        fill(255,0,0)
        image(photo,xb,0)
        scale(0.1)
        image(photostation, 14000, 6000)
    elif tilstand == "Missions":
        fill(0,255,0)
        rect(500,500,500,500)
    elif tilstand == "Tech":
        fill(0,0,255)
        rect(500,500,500,500)
    elif tilstand == "Compare":
        fill(0,0,255)
        rect(500,500,500,500)
        
tilstand = "hub"
timer = 0
tilvealg = 1
xb = 0
photo = None
timervalg = 0
timerfa = 0
effekter = []

def draw():
    global tilstand, timer, tilvealg, xb, timervalg, effekter, timerfa
    background(0)
    timerfa = timerfa + 1
    for i in effekter:
        i.tick()
        if timerfa > 30:
            i.farve()
            
    
    
    
    timer = timer + 1

    if tilstand == "hub":
        tilvealg = 1
        if timer > 30:
            timervalg = 0
        
        if mousePressed and mouseX < 640 and mouseY < 540 and timervalg == 0: #Venstre-op
            tilstand = "timeline"
            timer = 0
        elif mousePressed and mouseX < 640 and mouseY > 540 and timervalg == 0: #Venstre-ned
            tilstand = "Compare"
            timer = 0
        elif mousePressed and mouseX > 640 and mouseY < 540 and timervalg == 0: #Højre-op
            tilstand = "Missions"
            timer = 0
        elif mousePressed and mouseX > 640 and mouseY > 540 and timervalg == 0: #Højre-ned
            tilstand = "Tech"
            timer = 0
            
    elif tilstand == "timeline":
        if mousePressed and mouseX > 640 and mouseY > 540 and timer > 30: #Højre-ned
            tilstand = "hub"
            timer = 0
            timervalg = 1
            
    elif tilstand == "Missions":
        tilvealg = 3
        if mousePressed and mouseX < 640 and mouseY > 540 and timer > 30: #Venstre-ned
            tilstand = "hub"
            timer = 0
            timervalg = 1
            
    elif tilstand == "Tech":
        tilvealg = 4
        if mousePressed and mouseX < 640 and mouseY < 540 and timer > 30: #Venstre-op
            tilstand = "hub"
            timer = 0
            timervalg = 1
            
    elif tilstand == "Compare":
        tilvealg = 5
        if mousePressed and mouseX > 640 and mouseY < 540 and timer > 30: #Højre-op
            tilstand = "hub"
            timer = 0
            timervalg = 1
    
    if keyPressed and key != tilvealg:
        tilvealg = key
        if tilvealg == "2":
            tilstand = "timeline"
        elif tilvealg == "3":
            tilstand = "Missions"
        elif tilvealg == "4":
            tilstand = "Tech"
        elif tilvealg == "5":
            tilstand = "Compare"

            
    if keyPressed and key == "0" and timer > 20:
        if tilstand == "timeline":
            tilstand = "Missions"
            timer = 0
        elif tilstand == "Missions":
            tilstand = "Tech"
            timer = 0
        elif tilstand == "Tech":
            tilstand = "Compare"
            timer = 0
        elif tilstand == "compare":
            tilstand = "timeline"
            timer = 0
            
    if tilstand == "timeline":
        if mouseX < 1870:
            xb = xb + 5
        if mouseX > 50:
            xb = xb - 5
    
    
    slide(tilstand)
