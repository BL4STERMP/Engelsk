from Effekter import Stjerne


def setup():
    global photo, effekter, photostation, photorocket, photonout, photobench, photomoon
    fullScreen()
    size(1920,1080)
    photo = loadImage("Timeline.png")
    effekter = [Stjerne() for i in range(1000)]
    photostation = loadImage("SpaceStation.png")
    photorocket = loadImage("Rocket.png")
    photonout = loadImage("Astronout.png")
    photobench = loadImage("Malthe.png")
    photomoon = loadImage("Moon.png")
                          
    
def slide(tilstand):
    global x, photo, photostation, photorocket, photonout, photobench, photomoon
    
    if tilstand == "hub":
        fill(255,0,0)
        scale(0.2)
        
        scale(0.3)
        scale(10)
        rotate(320)
        image(photonout, 2100,1150)
        scale(0.5)
        image(photobench, 2000, 3000)
        scale(2)
        scale(0.5)
        image(photorocket,-400,150)
        scale(2)
        scale(0.5)
        image(photomoon,-2000,2300)
        image(photostation, 1300, 1500)
        
    elif tilstand == "timeline":
        fill(255,0,0)
        image(photo,xb,0)
        scale(0.1)
        image(photostation, 17000, 8000)
    elif tilstand == "Missions":
        fill(0,255,0)
        scale(0.1)
        image(photostation, 100, 8000)
    elif tilstand == "Tech":
        fill(0,0,255)
        scale(0.1)
        image(photostation, 100, 100)
        textSize(240)
        fill(255,255,255)
        text("1969: The Saturn V rocket, powered by the F-1 engine, is used to launch the Apollo 11 mission to the moon.",2500,550)
        text("1970: The Russian N-1 rocket, powered by the NK-33 engine, fails its fourth and final launch.",2500,550*2)
        text("1971: The Soviet Union launches the Salyut 1 space station, powered by the Soyuz 11A511 engine.",2500,550*3)
        text("1972: The Space Shuttle Main Engine (SSME) is tested for the first time.",2500,550*4)
        text("1981: The Space Shuttle is launched for the first time, powered by the SSME and two Solid Rocket Boosters.",2500,550*5)
        text("1986: The Soviet Union launches the Mir space station, powered by the Soyuz-U and Progress engines.",2500,550*6)
        text("1988: The Delta II rocket, powered by the RS-27 engine, is launched for the first time.",2500,550*7)
        text("1996: The Russian RD-180 engine is used for the first time on the Atlas IIAS rocket.",2500,550*8)
        text("1998: The X-43, an unmanned experimental hypersonic aircraft, sets a world speed record for a jet-powered aircraft using a scramjet engine.",2500,550*9)
        text("2004: The Falcon 1 rocket, powered by the Merlin 1 engine, is launched for the first time.",2500,550*10)
        text("2006: The Falcon 9 rocket, powered by the Merlin 1D engine, is launched for the first time.",2500,550*11)
        text("2010: The Space Shuttle Program ends after 30 years of service.",2500,550*12)
        text("2011: The Dragon spacecraft, powered by the Draco thrusters, is launched for the first time.",2500,550*13)
        text("2013: Blue Origin conducts the first successful test flight of the BE-3 engine.",2500,550*14)
        text("2015: The Falcon Heavy rocket, powered by 27 Merlin engines, is launched for the first time.",2500,550*15)
        text("2018: The New Glenn rocket, powered by seven BE-4 engines, is announced by Blue Origin.",2500,550*16)
        text("2021: The Starship spacecraft, powered by the Raptor engine, is tested for the first time.",2500,550*17)
    elif tilstand == "Compare":
        fill(0,0,255)
        scale(0.1)
        image(photostation, 17000, 100)
        
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
