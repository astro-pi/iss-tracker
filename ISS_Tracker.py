###ENSURE THAT TIME IS CORRECTLY SET###
###USE UP TO DAY TLE FILE###
#Python2.79##

from random import randint
from astro_pi import AstroPi
import ephem
import datetime
import time
## [...]
ap = AstroPi()

name = "ISS (ZARYA)";            
#line1 = "1 25544U 98067A   15178.42973832  .00011523  00000-0  17276-3 0  9998"
#line2 = "2 25544  51.6456  32.8760 0003760  98.7829 323.8559 15.55421066949635"

line1 = "1 25544U 98067A   15185.95963984  .00006354  00000-0  98170-4 0  9990"
line2 = "2 25544  51.6454 355.2696 0003202 121.3230  14.1346 15.55509232950800"

def countdown():
    for i in reversed(range(0, 6)):
        ap.show_letter(str(i))
        time.sleep(1)

countdown()        
ap.clear()
while True:
    temp = str(ap.get_temperature())
    pressure =  str(ap.get_pressure())
    orientation =  ap.get_orientation_degrees()

    time.sleep(0.5)
    tle_rec = ephem.readtle(name, line1, line2)
    tle_rec.compute()
    
    #convert to strings#
    lat2string = str(tle_rec.sublat)
    long2string = str(tle_rec.sublong)

    lati = lat2string.split(":")
    longt = long2string.split(":")

    ###Convert to floats to check the rangess

    lati[0] = float(lati[0])
    longt[0] = float(longt[0])
    print lati[0]
    print longt[0]
   

    ###Check the location###

    ###UK###
    if (lati[0] <= 53 and lati[0]>= 52) and (longt[0] >= -4 and longt[0]<= -1):
        print "United Kingdom"

        X = [255, 0, 0]  # Red
        O = [255, 255, 255]  # White

        UK = [
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O
        ]

        ap.set_pixels(UK)
        time.sleep(6)
        ap.show_message("Hello ISS, you are over the UK")
        ap.show_message("Hello ISS. How are you!", text_colour=[255, 0, 0])
        

    ###FRANCE###
    elif (lati[0] <= 49 and lati[0] >= 43) and (longt[0] >= -3 and longt[0] <= 6):    
        print "FRANCE"

        X = [255, 0, 0]  # Red 
        O = [255, 255, 255]  # White 
        b= [0,0, 255] #Blue
        French_Flag  = [ 
        b, b, b, O, O, O, X, X,
        b, b, b, O, O, O, X, X, 
        b, b, b, O, O, O, X, X, 
        b, b ,b, O, O, O, X, X, 
        b, b, b, O, O, O, X, X,
        b, b, b, O, O, O, X, X,
        b, b, b, O, O, O, X, X,
        b, b, b, O, O, O, X, X
        ]
        ap.set_pixels(French_Flag)

        time.sleep(6)
        ap.show_message("Bonjour!")
        ap.show_message("Bonjour Tim", text_colour=[255,255,0])

    ###GERMANY###
    elif (lati[0] <= 51 and lati[0] >= 50) and (longt[0] >= -10 and longt[0] <= 11):    
        print "GERMANY"

        X = [255, 0, 0]  # Red
        O = [0, 0, 0]  # Black
        Z = [255, 247, 0] #Yellow

        Germany = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, Z, Z, Z, Z, Z, Z, Z,   
        ]

        ap.set_pixels(Germany)
        time.sleep(6)
        ap.show_message("Hallo Tim. Wie geht es dir", text_colour=[255, 0, 255])

    ###SPAIN###
    elif (lati[0] <= 43 and lati[0] >= 37) and (longt[0] >= -7 and longt[0] <= 0):    
        print "SPAIN"

        O = [255,255,0]  # YELLOW
        X = [255,0,0] # RED
        B = [0,0,0] #BLACK

        Spain = [
        X,X,X,X,X,X,X,X, 
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,B,B,O,O,O,
        O,O,O,B,B,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X
        ]

        ap.set_pixels(Spain)
        time.sleep(6)
        ap.show_message("Hola ISS, Como esta", text_colour=[255, 255, 255])
        

    ###aUSTRIA##
    elif (lati[0] <= 48 and lati[0] >= 46) and (longt[0] >= 13 and longt[0] <= 16):    
        print "AUSTRIA"

        X = [255, 0, 0]  # Red 
        O = [255, 255, 255]  # White 
        Austria = [ 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X,
        ] 
        ap.set_pixels(Austria)
        time.sleep(5)
        ap.show_message("Hallo Tim , wie geht es dir?,  I'l be back!", text_colour=[255, 255, 255]) 

    ###SWITZLAND###
    elif (lati[0] <= 47 and lati[0] >= 46) and (longt[0] >= 6 and longt[0] <= 10):    
        print "SWITZLAND"
        X = [255, 0, 0]  # Red 
        O = [255, 255, 255]  # White 
        Austria = [ 
        X, X, X, O, O, X, X, X,
        X, X, X, O, O, X, X, X,
        X, X, X, O, O, X, X, X,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        X, X, X, O, O, X, X, X,
        X, X, X, O, O, X, X, X,
        X, X, X, O, O, X, X, X,
        ] 
        ap.set_pixels(Austria)
        time.sleep(8)
        ap.show_message("Hej Tim hur mår du?", text_colour=[150, 200, 140])

    ###ROMANIA###
    elif (lati[0] <= 47 and lati[0] >= 43) and (longt[0] >= 23 and longt[0] <= 28):    
        print "ROMANIA"
        X = [0, 0, 255]  #blue    
        O = [255, 240, 10]  # Yellow  
        T = [255, 0, 0,] # red 

        Romania = [  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        ]
        ap.set_pixels(Romania)
        time.sleep(5)
        ap.show_message("Alo ISS dla Romania", text_colour=[255, 222, 255])

    ###SLOVAKIA###
    elif (lati[0] <= 49 and lati[0] >= 48) and (longt[0] >= 17 and longt[0] <= 21):    
        print "SOLVAKIA"
        X = [255, 0, 0]  # Red  
        O = [255, 255, 255]  # white
        V = [0, 0, 255]#blue
         
        sOL = [ 
        O, O, O, O, O, O, O, O, 
        O, X, X, X, O, O, O, O, 
        O, X, O, X, O, O, O, O, 
        V, O, O, O, V, V, V, V, 
        V, X, V, X, V, V, V, V, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        ] 
        ap.set_pixels(sOL)
        time.sleep(5)
        ap.show_message("Ahoj ISS", text_colour=[255, 222, 255])

    ###POLAND###
    elif (lati[0] <= 54 and lati[0] >= 49) and (longt[0] >= 14 and longt[0] <= 23):    
        print "POLAND"

        W = [255,255,255] # White
        R = [255,0,0] # Red

        Poland = [
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        ]
        ap.set_pixels(Poland)
        time.sleep(5)
        ap.show_message("Czesc ISS powitanie to Poland", text_colour=[255, 222, 255])

    ###BELARUS###
    elif (lati[0] <= 53 and lati[0] >= 51) and (longt[0] >= 23 and longt[0] <= 30):    
        print "BELARUS"

        X = [0, 255, 0]  # Green
        O = [255, 0, 0]  # red
        L = [255, 255, 255] #white

        Belarus = [
        L, O, O, O, O, O, O, O,
        O, L, O, O, O, O, O, O,
        L, O, O, O, O, O, O, O,
        O, L, O, O, O, O, O, O,
        L, O, O, O, O, O, O, O,
        O, L, X, X, X, X, X, X,
        L, O, X, X, X, X, X, X,
        O, L, X, X, X, X, X, X,
        ]

        ap.set_pixels(Belarus)
        time.sleep(9)
        ap.show_message("Dobry dzien ISS, mianie zavucdzef Jeff", text_colour=[0, 222, 0])
    
    ##namBIA###
    elif (lati[0] <= -17 and lati[0] >= -28) and (longt[0] >= 11 and longt[0] <= 19):    
        print "NAMIBIA"
        X = [255,0,0]  #  Red 
        O = [255, 240, 10]  # Yellow 
        T = [0,0,153] # Blue

        Nambia = [ 
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        ]
        ap.set_pixels(Nambia)
        time.sleep(5)
        ap.show_message("Hi ISS we speak, Germanm English and Afrokan", text_colour=[255, 0, 0])

        
    ###ANGOLA###
    elif (lati[0] <= -6 and lati[0] >= -17) and (longt[0] >= 12 and longt[0] <= 23):    
        print "ANGOLA"
        X = [255, 0, 0]  # Red 
        O = [255, 240, 10]  # Yellow  
        T = [0, 0, 0,] # Black 

        Angola_Flag = [  
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, O, O, X, X, X, 
        T, T, T, O, O, T, T, T,  
        T, T, T, T, T, T, T, T, 
        T, T, T, T, T, T, T, T, 
        T, T, T, T, T, T, T, T, 
        ]
        ap.set_pixels(Angola_Flag)
        time.sleep(8)
        ap.show_message("Ola ISS", text_colour=[255, 0, 0])

             
    ###DR CONGO###
    elif (lati[0] <= 4 and lati[0] >= -8) and (longt[0] >= 19 and longt[0] <= 29):    
        print "DR CONGO"
        X = [0,153,255]  # blue  
        O = [255,255,0]  # Yellow 
        T = [255,0,0] # red

        dr_congo = [
        X,X,X,X,X,X,T,T,
        X,O,X,X,X,T,T,X,
        X,X,X,X,T,T,X,X,
        X,X,X,T,T,X,X,X,
        X,X,T,T,X,X,X,X,
        X,T,T,X,X,X,X,X,
        T,T,X,X,X,X,X,X,
        T,X,X,X,X,X,X,X,
        ] 

        ap.set_pixels(dr_congo)
        time.sleep(6)
        ap.show_message("Olá Tim. Como vai", text_colour=[255, 0, 0])

    ###SOUTH SUDAN###
    elif (lati[0] <= 9 and lati[0] >= 4 ) and (longt[0] >= 23 and longt[0] <= 35):    
        print "SOUTH SUDAN"
        X = [255, 0, 0]  # Red
        O = [255, 255, 255]  # White
        
        test = [
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,X,X,O,O,O,
        O,O,O,X,X,O,O,O,
        O,O,O,X,X,O,O,O,
        O,O,O,X,X,O,O,O,
        O,O,O,X,X,O,O,O,
        O,O,O,X,X,O,O,O,
        ]
        ap.set_pixels (test)

    ###SUDAN###
    elif (lati[0] <= 21 and lati[0] >= 9 ) and (longt[0] >= 25 and longt[0] <= 34):    
        print "SUDAN"

        X = [0, 255, 0]  # Green
        O = [0, 0, 0]  # Black
        Z = [255, 255, 255] #white
        F = [255, 0, 0] #red

        Sudan = [
        X, F, F, F, F, F, F, F,
        X, X, F, F, F, F, F, F,
        X, X, X, F, F, F, F, F,
        X, X, X, X, Z, Z, Z, Z,
        X, X, X, X, Z, Z, Z, Z,
        X, X, X, O, O, O, O, O,
        X, X, O, O, O, O, O, O,
        X, O, O, O, O, O, O, O,]

        ap.set_pixels(Sudan)
        time.sleep(6)
        ap.show_message("Halo from Sudan")

    ###SAUDI ARABIA###
    elif (lati[0] <= 31 and lati[0] >= 20 ) and (longt[0] >= 36 and longt[0] <= 54):    
        print "SAUDI ARABIA"

        X = [0, 255, 0]  # Green
        O = [255, 255, 255,] # White

        SaudiArab = [
        X, X, X, X, X, X, X, X,
        X, O, X, O, O, O, X, X,
        X, O, O, O, O, O, O, X,
        X, O, O, O, X, X, X, X, 
        X, X, X, X, X, O, X, X, 
        X, O, O, O, O, O, O, X, 
        X, X, X, X ,X, X, X, X, 
        X, X, X, X, X, X, X, X,
        ]

        ap.set_pixels(SaudiArab)
        time.sleep(6)
        ap.show_message("Hi Guys from Saudi Arabia")

    ###yEMEN###
    elif (lati[0] <= 17 and lati[0] >= 13 ) and (longt[0] >= 43 and longt[0] <= 52):    
        print "Yemen"
        X = [255, 0, 0]  # Red  
        O = [0, 0, 0]  # WHITE 
        B = [255,255,255] # black
         

        Yemenese_Flag = [ 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O,    
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, 
        B, B, B, B, B, B, B, B, 
        ] 
        ap.set_pixels(Yemenese_Flag)
        time.sleep(6)
        ap.show_message("Hi Guys from Yemen")
        
        

    ###yemen###
    elif (lati[0] <= 17 and lati[0] >= 16) and (longt[0] >= 43 and longt[0] <= 53):    
        print "yemen"
        X = [255, 0, 0]  # Red  
        O = [0, 0, 0]  # WHITE 
        B = [255,255,255] # black
         

        Yemenese_Flag = [ 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O,    
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, 
        B, B, B, B, B, B, B, B, 
        ] 
        ap.set_pixels(Yemenese_Flag)
       

    ###IRAQ###
    elif (lati[0] <= 37 and lati[0] >= 29) and (longt[0] >= 42 and longt[0] <= 46):    
        print "IRAQ"
        R = [255,0,0]  # RED
        B = [0,0,0]  # BLACK
        W = [255,255,255] #WHITE
        G = [0,255,0] #GREEN

        IRAQ = [ 
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        W,W,W,W,W,W,W,W, 
        W,G,W,W,G,G,W,W, 
        W,W,G,W,W,W,G,W, 
        W,W,W,W,W,W,W,W, 
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        ]
        ap.set_pixels(IRAQ)

    ###IRAN###
    elif (lati[0] <= 35 and lati[0] >= 25) and (longt[0] >= 51 and longt[0] <= 61):    
        print "IRAN"
        X = [255, 0, 0]  # Red  
        O = [255, 255, 255] # White
        V = [0, 255, 0] # Green
        B = [0,0,0] #Black

        Iran = [ 
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        O, O, O, O, O, O, O, O,
        O, O, V, V, V, V, O, O, 
        O, O, V, V, V, V, O, O, 
        O, O, O, O, O, O, O, O,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        ] 
        ap.set_pixels(Iran) 


    ####Turkmenistan###
    elif (lati[0] <= 41 and lati[0] >= 35) and (longt[0] >= 54 and longt[0] <= 62):    
        print "Turkmenistan"
        X = [0, 255, 255,]#geen
        O = [0, 0, 255]  # Blue
        Z = [255, 247, 0] #Yellow
        U = [255, 0, 0] #RED
        I = [255, 255, 255] # WHITE

        Turkmen = [
        X, U, I, U, X, X, X, X,
        X, U, U, U, I, X, I, X,
        X, U, X, U, X, I, X, I,
        X, U, U, U, I, I, X, I,
        X, U, X, U, X, X, I, X,
        X, U, U, U, X, X, X, X,
        X, U, X, U, X, X, X, X,
        X, U, U, U, X, X, X, X,
        ]

        ap.set_pixels(Turkmen)
        time.sleep(8)
        ap.show_message("your over Turkmenistan. sorry I couldn't find a translation", text_colour=[255, 100, 0])

    ###AFGANISTAN###
    elif (lati[0] <= 35 and lati[0] >= 31) and (longt[0] >= 61 and longt[0] <= 69):    
        print "AFGFHAN"

        X = [0, 255, 0]  # Green
        F = [50, 50, 50] #black
        B = [255, 0, 0] #RED
        S = [255, 255, 255] #WHITE
        afGHAN = [
        F, F, F, B, B, X, X, X,
        F, F, F, B, B, X, X, X,
        F, F, F, S, S, X, X, X,
        F, F, S, S, S, S, X, X,
        F, F, S, S, S, S, X, X,
        F, F, F, S, S, X, X, X,
        F, F, F, B, B, X, X, X,
        F, F, F, B, B, X, X, X,
        ]

        ap.set_pixels(afGHAN)
        time.sleep(7)
        ap.show_message("UTF8 does not support Arabic symbols, sorryPrivet, Hi from down below", text_colour=[150, 0, 255])

    ###GUINEA###
    elif (lati[0] <= 12 and lati[0] >= 7) and (longt[0] >= -13 and longt[0] <= -8):    
        print "GUINEA"

        X = [255, 0, 0] 
        F = [0, 235, 0]
        G = [255, 240, 10]

        Guinea_Flag=[
        X, X, X, G, G, G, F, F,   
        X, X, X, G, G, G, F, F,  
        X, X, X, G, G, G, F, F,   
        X, X, X, G, G, G, F, F,  
        X, X, X, G, G, G, F, F, 
        X, X, X, G, G, G, F, F, 
        X, X, X, G, G, G, F, F,   
        X, X, X, G, G, G, F, F,   
        ]
        ap.set_pixels(Guinea_Flag)

                
    ###SOUTH AFRICA###
    elif (lati[0] <= -28 and lati[0] >= -33) and (longt[0] >= 16 and longt[0] <= 32):    
        print "SOUTH AFRICA"

        x = [0, 255, 0]  # Green
        o = [0, 0, 0]  # black
        z = [255, 247, 0] #Yellow
        r = [255,51,0] # red
        b = [51,102,255] # blue
        w = [255,255,255] # white

        SouthAfrica = [
        x,x,w,r,r,r,r,r,
        x,x,x,w,r,r,r,r,
        z,x,x,x,w,w,w,w,
        o,z,x,x,x,x,x,x,
        o,z,x,x,x,x,x,x,
        z,x,x,x,w,w,w,w,
        x,x,x,w,b,b,b,b,
        x,x,x,w,b,b,b,b,
        ]

        ap.set_pixels(SouthAfrica)
        time.sleep(6)
        ap.show_message("Hi Tim jou vlieg oor pragtige Suid-Afrika", text_colour=[255, 0, 0])
    
    ###ETHIOPIA###
    elif (lati[0] <= 13 and lati[0] >= 4) and (longt[0] >= 36 and longt[0] <= 44):    
        print "ETHIOPIA"

        X = [0, 255, 0]  # Green
        O = [255,0,0] # Red
        Z = [255, 247, 0] #Yellow
        S = [0,0,255] #Blue
        Ethiopia = [
        X,X,X,X,X,X,X,X,
        X,X,X,S,S,X,X,X,
        X,X,X,S,S,X,X,X,
        Z,Z,S,Z,Z,S,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        ]

        ap.set_pixels(Ethiopia)
        time.sleep(6)
        ap.show_message("Hi Guys from Ethiopia, how is it up there on the ISS?")

    ###ARGENTINA###
    elif (lati[0] <= -22 and lati[0] >= -54) and (longt[0] >= -67 and longt[0] <= -65):    
        print "ARGENTINA"

        X = [0, 200, 255] # Turquoise 100, 225, 221 
        O = [255, 255, 255]  # White 
        Y = [255, 200, 0] # Orangey-Yellow
        Argentinian_Flag = [ 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        O, O, O, O, O, O, O, O, 
        O, O, O, Y, Y, O, O, O, 
        O, O, O, Y, Y, O, O, O, 
        O, O, O, O, O, O, O, O, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        ]
        ap.set_pixels(Argentinian_Flag)
        time.sleep(8)
        ap.show_message("Saludos, Tim, ¿Cómo estás?", text_colour=[0, 255, 255])

    ###PERU###
    elif (lati[0] <= -4 and lati[0] >= -17) and (longt[0] >= -80 and longt[0] <= -69):    
        print "PERU"
        X = [255, 0, 0]  # Red  
        O = [255, 255, 255]  #White  
        T = [0, 0, 0,] # Black

        Peruvian_Flag = [ 
        X, X, X, O, O, X, X, X, 
        X, X, X, O, O, X, X, X, 
        X, X, X, O, O, X, X, X, 
        X, X, X, O, O, X, X, X, 
        X, X, X, O, O, X, X, X, 
        X, X, X, O, O, X, X, X, 
        X, X, X, O, O, X, X, X, 
        X, X, X, O, O, X, X, X, 
        ] 
        ap.set_pixels(Peruvian_Flag)
        time.sleep(8)
        ap.show_message("Hola ISS desde peru abajo", text_colour=[200, 150, 20])

        
    ###NIGERIA###
    elif (lati[0] <= 13 and lati[0] >= 4 ) and (longt[0] >= 4  and longt[0] <= 8):    
        print "NIGERIA"

        X = [0, 255, 0]  # Green
        O = [0, 0, 0 ]  # 
        Z = [255, 247, 0] #Yellow

        question_mark = [
        X, X, X, Z, Z, X, X, X,
        X, X, Z, O, O, Z, X, X,
        X, Z, O, O, O, O, Z, X,
        Z, O, O, O, O, O, O, Z,
        Z, O, O, O, O, O, O, Z,
        X, Z, O, O, O, O, Z, X,
        X, X, Z, O, O, Z, X, X,
        X, X, X, Z, Z, X, X, X,
        ]

        ap.set_pixels(question_mark)

        time.sleep(6)
        ap.show_message("Hello Tim, how are you", text_colour=[255, 0, 0])

    ###NIGER###
    elif (lati[0] <= 20 and lati[0] >= 13 ) and (longt[0] >= 7  and longt[0] <= 14):    
        print "NIGER"

        X = [0, 255, 0]  # Green
        W = [255, 255, 255]  # White
        Z = [255, 110, 0] # Orange

        Niger = [
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z,
        W,W,W,W,W,W,W,W,
        W,W,W,Z,Z,W,W,W,
        W,W,W,Z,Z,W,W,W,
        W,W,W,W,W,W,W,W,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        ]

        ap.set_pixels(Niger)

    ###CHAD###
    elif (lati[0] <= 22 and lati[0] >= 11 ) and (longt[0] >= 15  and longt[0] <= 22):    
        print "CHAD"

        X = [255, 0, 0]  # Red
        O = [0, 0, 255]  # Blue
        Z = [255, 247, 0] #Yellow

        Chad = [
        O, O, Z, Z, Z, Z, X, X,
        X, O, Z, Z, Z, Z, X, X,
        X, O, Z, Z, Z, Z, X, X,
        Z, O, Z, Z, Z, Z, X, X,
        Z, O, Z, Z, Z, Z, X, X,
        X, X, Z, Z, Z, Z, X, X,
        X, X, Z, Z, Z, Z, X, X,
        X, X, Z, Z, Z, Z, X, X,
        ]

        ap.set_pixels(Chad)
        time.sleep(8)
        ap.show_message("Bonjour ISS de Chad", text_colour=[0, 255, 255])

    ###LIBYA###
    elif (lati[0] <= 33 and lati[0] >= 19) and (longt[0] >= 11  and longt[0] <= 23):    
        print "LIBYA"

        X = [0, 255, 50]  # Green
        O = [0, 0, 0]  # BLACK
        Z = [255, 247, 0] #Yellow
        R = [255, 255, 255] #WHITE
        V = [255, 0, 0] #RED

        lIB = [
        V, V, V, V, V, V, V, V,
        V, V, V, V, V, V, V, V,
        O, O, O, R, O, O, O, O,
        O, O, R, O, O, R, O, O,
        O, O, R, O, O, O, O, O,
        O, O, O, R, O, O, O, O,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        ]

        ap.set_pixels(lIB)
        time.sleep(8)
        ap.show_message("Hi ISS this is Libya", text_colour=[255, 255, 255])

    ###TURKEY###
    elif (lati[0] <= 41 and lati[0] >= 37) and (longt[0] >= 28  and longt[0] <= 44):    
        print "TURKEY"

        x = [255,0, 0]  # red
        o = [255,255,255]  # yellow

        Turkey = [
        x,x,x,x,x,x,x,x,
        x,x,o,o,x,x,x,x,
        x,o,x,x,x,o,x,x,
        x,o,x,x,o,o,o,x,
        x,o,x,x,x,o,x,x,
        x,x,o,o,x,x,x,x,
        x,x,x,x,x,x,x,x,
        x,x,x,x,x,x,x,x
        ]
        ap.set_pixels(Turkey)
        time.sleep(8)
        ap.show_message("Merhaba ISS senin birkus uzerinde ucan aludos,", text_colour=[0, 255, 255])

    ###UKRAINE### 
    elif (lati[0] <= 51 and lati[0] >= 46) and (longt[0] >= 23 and longt[0] <= 37):    
        print "UKRAINE"

        X = [0, 0, 255]  # Blue  
        O = [255, 240, 10]  # Yellow 

        Ukraine_Flag = [ 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O,] 
         
        ap.set_pixels(Ukraine_Flag)
        time.sleep(8)
        ap.show_message("Hi Tim and ISS team from Ukraine")

    ###RUSSIA###
    elif (lati[0] <= 74 and lati[0] >= 51) and (longt[0] >= 34 and longt[0] <= 38):    
        print "RUSSIA"

        X = [255, 0, 0]  # Red 
        O = [255, 255, 255]  # White 
        Y = [13, 0, 255] # Blue
         
        RUSSIAN_Flag = [ 
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O, 
        Y, Y, Y, Y, Y, Y, Y, Y, 
        Y, Y, Y, Y, Y, Y, Y, Y, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X 
        ] 
        ap.set_pixels(RUSSIAN_Flag)

        time.sleep(4)
        ap.show_message("Privet, ISS Komanda, kak dela??", text_colour=[0, 0, 255])

    ###KAZAHSTAN###   
    elif (lati[0] <= 52 and lati[0] >= 42) and (longt[0] >= 49 and longt[0] <= 80):    
        print "KASAHSTAN"

        X = [0, 255, 0]  # Green
        Z = [255, 247, 0] #Yellow
        H = [23, 166, 255] #LIGHT BLUE
        kaz = [
        H, Z, H, H, H, H, H, H,
        H, Z, H, H, H, H, H, H,
        H, Z, H, H, Z, Z, H, H,
        H, Z, H, Z, Z, Z, Z, H,
        H, Z, H, Z, Z, Z, Z, H,
        H, Z, H, H, Z, Z, H, H,
        H, Z, H, H, H, H, H, H,
        H, Z, H, H, H, H, H, H,
        ]
        ap.set_pixels(kaz)

        time.sleep(8)
        ap.show_message("Hi team ISS from Kasahstan")

    ###MONGLOIA###
    elif (lati[0] <= 50 and lati[0] >= 43) and (longt[0] >= 88 and longt[0] <= 115):    
        print "MONGLOIA"

        X = [255, 0, 0]  # Red
        O = [0, 0, 255]  # Blue
        Z = [255, 247, 0] #Yellow

        mONGOLIA = [
        X, X, X, O, O, X, X, X,
        X, Z, X, O, O, X, X, X,
        X, X, X, O, O, X, X, X,
        X, Z, X, O, O, X, X, X,
        X, Z, X, O, O, X, X, X,
        X, X, X, O, O, X, X, X,
        X, Z, X, O, O, X, X, X,
        X, X, X, O, O, X, X, X,
        ]

        ap.set_pixels(mONGOLIA)
        
    ###CHINA###
    elif (lati[0] <= 48 and lati[0]>= 23) and (longt[0] >= 87 and longt[0]<= 123):
        print "CHINA"
        X = [255, 0, 0]  # Red  
        O = [255, 240, 10]  # Yellow 
        
        Chinese_Flag = [ 
        X, X, X, O, X, X, X, X, 
        X, O, O, X, O, X, X, X, 
        X, O, O, X, O, X, X, X, 
        X, X, X, O, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X,X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        ] 
        ap.set_pixels(Chinese_Flag)
        time.sleep(8)
        ap.show_message("Nin hao ISS this is China", text_colour=[0, 255, 255])

    ###MALASYSIA###
    elif (lati[0] <= 6 and lati[0]>= 1) and (longt[0] >= 100 and longt[0]<= 104):
        print "MALASYSIA"

        X = [20, 30, 255]  # Turquoise  
        O = [255, 240, 10]  # Yellow 
        T = [0, 0, 0,] # Black

        Malaysia = [ 
        T, X, X, X, X, X, X, X, 
        T, T, X, X, X, X, X , X, 
        T, T, T, X, X, X, X, X, 
        T, T, T, T, O, O, O, O, 
        T, T, T, T, O, O, O, O, 
        T, T,T, X, X, X, X, X, 
        T, T, X, X, X, X, X, X, 
        T, X, X, X, X, X, X, X, 
        ] 
        ap.set_pixels(Malaysia)

    ###PNG###
    elif (lati[0] <= -0 and lati[0]>= -10) and (longt[0] >= 130 and longt[0]<= 150):
        print "PNG"
        X = [255, 0, 0]  # Red  
        O = [255, 240, 10]  # Yellow 
        V = [0, 0, 0] # Black

        png = [ 
        V, X, X, X, X, X, X, X,
        V, V, X, X, O, O, O, X,
        V, V, V, X, O, O, O, X,
        V, V, V, V, O, O, O, X,
        V, V, V, V, V, X, X, X,
        V, V, V, V, V, V, X, X,
        V, V, V, V, V, V, V, X,
        V, V, V, V, V, V, V, V, 
        ] 
        ap.set_pixels(png) 

        
            

    ###0Z###   USE THIS ONE ####
    elif (lati[0] >= -38 and lati[0] <= -16) and (longt[0] >= 115 and longt[0] <= 146):    
        print "OZ"
        T = [255, 255, 255]  # White  
        O = [255, 0, 0]  # Red 
        X = [0, 0, 255] # Blue

        OZ = [ 
        X, X, O, X, X, X, X, X, 
        X, X, O, X, X, X, X , X, 
        O, O, O, O, O, X, X, X, 
        X, X, O, X, X, X, X, X, 
        X, X, O, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, T, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        ] 
        ap.set_pixels(OZ)
        time.sleep(8)
        ap.show_message("What up Bruce put that Banger on the Barbie!?", text_colour=[0, 255, 0]) 

    ###TAZ###
    elif (lati[0] <= -40 and lati[0] >= -43) and (longt[0] >= 144 and longt[0] <= 148):    
        print "TAZMANIA"
        X = [20, 30, 255]  # turquise 
        O = [255, 0, 0]  # Yellow 
        T = [0, 0, 255] # BlUE
        G = [0, 255, 0] # Green
        L = [255, 255, 255] #WHITE
        TAZ = [ 

        G, G, G, G, G, G, G, G,
        G, G, G, G, G, G, G, G, 
        G, G, G, L, L, L, G, G,
        L, L, L, O, O, L, L, L,
        L, L, L, O, O, L, L, L,
        T, T, T, L, L, L, T, T,
        T, T, T, T, T, T, T, T,
        T, T, T, T, T, T, T, T,
        ] 
        ap.set_pixels(TAZ)

    ###NEW ZELAND###
    elif (lati[0] <= -35 and lati[0] >= -46) and (longt[0] >= 166 and longt[0] <= 177):    
        print "OZ"
        R = [255, 0, 0]  # Red 
        B = [0, 0, 255]  # Blue 
        W = [255, 255, 255] # White

        New_Zealand_Flag = [ 
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,W,B,B,
        B,B,B,B,B,B,R,B,
        B,B,B,B,W,B,B,B,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,R,B,B,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        ] 
        ap.set_pixels(New_Zealand_Flag)
        time.sleep(8)
        ap.show_message("Hi from the land of the Hobbit and LOTR", text_colour=[255, 255, 200])
        ap.show_message("You shall not pass!!!", text_colour=[255, 255, 200])

    ###NORTH KOREA WARNING
    elif (lati[0] <= 41 and lati[0] >= 38 ) and (longt[0] >= 124 and longt[0] <= 128):    
        print "NORTH KOREA"

        FLASH = 5000

        while FLASH > 0:   
            x = randint(0, 7)
            y = randint(0, 7)
            r = randint(0, 255)
            g = randint(0, 40)
            b = randint(0, 0)
            ap.set_pixel(x, y, r, g, b)
            FLASH = FLASH - 1

    ###SOUTH KOREA
    elif (lati[0] <= 37 and lati[0] >= 34 ) and (longt[0] >= 125 and longt[0] <= 129):    
        print "SOUTH KOREA"
        X = [255, 0, 0]  # Red  
        O = [0, 0, 255]  # Blue 
        Y = [0, 0, 0,] # White
        Z = [255, 255, 255] # Black

        sk = [ 
        Y,Y,Z,Y,Y,Z,Y,Y,
        Y,Z,Y,Y,Y,Y,Z,Y,
        Z,Y,Y,Y,Y,Y,Y,Z,
        Y,Y,Y,X,X,Y,Y,Y,
        Y,Y,Y,X,X,Y,Y,Y,
        Z,Y,Y,Y,Y,Y,Y,Z,
        Y,Z,Y,Y,Y,Y,Z,Y,
        Y,Y,Z,Y,Y,Z,Y,Y,
        ]
        ap.set_pixels(sk) 

        

    ###JAPAN
    elif (lati[0] <= 46 and lati[0] >= 31 ) and (longt[0] >= 131 and longt[0] <= 142):    
        print "JAPAN"

        X = [255, 0, 0]  # Red
        O = [255, 255, 255]  # White

        Japanese_Flag = [
        O, O, O, O, O, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, X, X, X, X, O, O,
        O, X, X, X, X, X, X, O,
        O, X, X, X, X, X, X, O,
        O, O, X, X, X, X, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, O, O, O, O, O]

        ap.set_pixels(Japanese_Flag)
        time.sleep(7)
        ap.show_message("Kon'nichiwa, Timu, ogenkidesuka?", text_colour=[0, 0, 255])

    ###MALI###
    elif (lati[0] <= 24 and lati[0] >= 15 ) and (longt[0] >= -6 and longt[0] <= 3):    
        print "MALI"

        X = [0, 255, 0]  # Green
        Y = [255,0,0] # Red
        Z = [255, 247, 0] #Yellow

        mALI = [
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        ]
        ap.set_pixels(mALI)
        time.sleep(6)
        ap.show_message("Bonjour Tim comment allez-vous", text_colour=[255, 0, 0])

    ###MAURITANIA###
    elif (lati[0] <= 22 and lati[0] >= 15 ) and (longt[0] >= -12 and longt[0] <= -5):    
        print "MAURITANIA"
        X = [74, 143, 34]  # Green 
        O = [255, 240, 10]  # Yellow 
        T = [0, 0, 0,] # Black

        Maratania = [ 
        X, X, X, X, X, X, X, X, 
        X, O, X, O, X, O, X , X, 
        X, O, X, X, X, O, X, X, 
        X, X, O, X, O, X, X, X, 
        X, X, X, O, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        ] 
        ap.set_pixels(Maratania) 


    ###Algeria###
    elif (lati[0] <= 35 and lati[0] >= 23) and (longt[0] >= -1 and longt[0] <= 11):    
        print "Algeria"
        X = [255, 0, 0]  # Red 
        O = [255, 255, 255]  # White 
        T = [0, 128, 0,] # Green
        Algeria_Flag = [ 
        T, T, T, T, O, O, O, O, 
        T, T, T, T, O, O, O, O,
        T, T, T, T, O, O, O, O,  
        T, T, T, X, X, O, O, O, 
        T, T, T, X, X, O, O, O, 
        T, T, T, T, O, O, O, O,
        T, T, T, T, O, O, O, O, 
        T, T, T, T, O, O, O, O, 
        ] 
        ap.set_pixels(Algeria_Flag) 
       

    ###GREECE###
    elif (lati[0] <= 40 and lati[0] >= 36) and (longt[0] >= 20 and longt[0] <= 23):    
        print "GREECE"
        B = [0,0,255]  # BLue
        W = [255,255,255] #WHITE

        greece = [ 
        B,W,B,B,B,B,B,B,
        W,W,W,W,W,W,W,W,
        B,W,B,B,B,B,B,B,
        W,W,W,W,W,W,W,W,
        B,B,B,B,B,B,B,B,
        W,W,W,W,W,W,W,W,
        B,B,B,B,B,B,B,B,
        W,W,W,W,W,W,W,W,
        ]
        ap.set_pixels(greece)

    ###THAILAND###
    elif (lati[0] <= 19 and lati[0] >= 12) and (longt[0] >= 97 and longt[0] <= 103):    
        print "THAILAND"
        X = [0,0,255]  # blue 
        O = [0,0,0]  # white 
        T = [255,0,0] # red

        tLAND = [ 
        T, T, T, T, T, T, T, T, 
        T, T, T, T, T, T, T , T, 
        O, O, O, O, O, O, O, O, 
        X, X, X,X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X,X, X, X, X, X, X, 
        O, O, O, O, O, O, O, O, 
        T, T, T, T, T, T, T, T, 
        ] 
        ap.set_pixels(tLAND) 

    ###INDONESIA###
    elif (lati[0] <= 0 and lati[0] >= -6) and (longt[0] >= 119 and longt[0] <= 123):    
        print "INDONESIA"
        X = [255, 0, 0]  # Red
        O = [255, 255, 255]  # White
        
        iNDO = [
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        ]
        ap.set_pixels(iNDO)    

    ###MAYLASIA###
    elif (lati[0] <= 6 and lati[0] >= 1) and (longt[0] >= 99 and longt[0] <= 116):    
        print "MAYLASIA"
        X = [20, 30, 255]  # Turquoise  
        O = [255, 240, 10]  # Yellow 
        T = [0, 0, 0,] # Black

        Malaysia = [ 
        T, X, X, X, X, X, X, X, 
        T, T, X, X, X, X, X, X, 
        T, T, T, X, X, X, X, X, 
        T, T, T, T, O, O, O, O, 
        T, T, T, T, O, O, O, O, 
        T, T, T, X, X, X, X, X, 
        T, T, X, X, X, X, X, X, 
        T, X, X, X, X, X, X, X, 
        ] 
        ap.set_pixels(Malaysia)

    ###DENMARK### 
    elif (lati[0] <= 57 and lati[0] >= 54) and (longt[0] >= 7 and longt[0] <= 11):    
        print "DENMARK"        

        X = [255, 255, 255]  # WHITE
        O = [255, 0, 0]  #RED
        T = [0, 0, 0,] # Black

        Denmark = [ 
        O, O, X, X, O, O, O, O, 
        O, O, X, X, O, O, O, O, 
        O, O, X, X, O, O, O, O, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        O, O, X, X, O, O, O, O, 
        O, O, X, X, O, O, O, O, 
        O, O, X, X, O, O, O, O, 
        ] 
        ap.set_pixels(Denmark)
        time.sleep(8)
        ap.show_message("Hej ISS din over landet af lego", text_colour=[255, 0,255])
      

    ###USA###
    elif (lati[0] <= 48 and lati[0] >= 25) and (longt[0] >= -124 and longt[0] <= -80):    
        print "HAWAII"

        X = [255, 0, 0]  # Red 
        O = [255, 255, 255]  # White 
        W = [0, 0, 255] #blue
        usa = [ 
        O, W, W, W, W, W, W, W, 
        W, W, O, X, X, X, X, X, 
        O, W, W, W, W, W, W, W,
        X, X, X, X, X, X, X, X, 
        W, W, W, W, W, W, W, W, 
        X, X, X, X, X, X, X, X, 
        W, W, W, W, W, W, W, W, 
        X, X, X, X, X, X, X, X,  
        ] 
        ap.set_pixels(usa)
        time.sleep(9)
        ap.show_message ("Wad up bro?", text_colour=[100, 100, 255])

    ###HAWAII###
    elif (lati[0] <= 22 and lati[0] >= 18) and (longt[0] >= -160 and longt[0] <= -154):    
        print "HAWAII"

        X = [255, 255, 255]  # White
        O = [0, 0, 255]  # Blue
        Z = [255, 0, 0] #Red 

        HW50 = [
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, Z, Z, Z, Z, Z, Z, Z,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, Z, Z, Z, Z, Z, Z, Z,
        ]

        ap.set_pixels(HW50)
        time.sleep(5)
        ap.show_message("Ahloa ISS Surf's up", text_colour=[0, 255, 0]) 

    ###CANADA###
    elif (lati[0] <= 77 and lati[0] >= 46) and (longt[0] >= -133 and longt[0] <= -53):    
        print "CANADA"

        X = [255, 0, 0]  # Red 
        O = [255, 255, 255]  # White 
         
        cAN = [ 
        X, O, O, O, O, O, O, X, 
        X, O, O, X, X, O, O, X, 
        X, O, X, X, X, X, O, X, 
        X, O, O, X, X, O, O, X, 
        X, O, O, X, X, O, O, X,
        X, O, O, X, X, O, O, X, 
        X, O, O, O, O, O, O, X,
        X, O, O, O, O, O, O, X,
        ] 
        ap.set_pixels(cAN)
        time.sleep(6)
        ap.show_message("HI tim I hope you like pancakes and maple syrup try canada's pankcakes with the winter wether we have in winter", text_colour=[0, 0, 255]) 
    

    ###BRAZIL###
    elif (lati[0] <=1 and lati[0] >= -13) and (longt[0] >= -69 and longt[0] <= -38):    
        print "BRAZIL"    

        X = [0, 255, 0]  # Green
        O = [0, 0, 255]  # Blue
        Z = [255, 247, 0] #Yellow

        Brazil = [
        X, X, X, Z, Z, X, X, X,
        X, X, Z, O, O, Z, X, X,
        X, Z, O, O, O, O, Z, X,
        Z, O, O, O, O, O, O, Z,
        Z, O, O, O, O, O, O, Z,
        X, Z, O, O, O, O, Z, X,
        X, X, Z, O, O, Z, X, X,
        X, X, X, Z, Z, X, X, X,
        ]

        ap.set_pixels(Brazil)
        time.sleep(6)
        ap.show_message("Ola ISS, Como vai", text_colour=[255, 0, 0])

    ###Bol###
    elif (lati[0] <= -11 and lati[0] >= -22) and (longt[0] >= -69 and longt[0] <= -58):    
        print "Bolivia"
        X = [255, 0, 0]  # Red  
        O = [255, 240, 10]  # Yellow 
        M = [0, 255, 0] # Green

        Bol = [ 
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        M, M, M, M, M, M, M, M,
        M, M, M, M, M, M, M, M,
        M, M, M, M, M, M, M, M,
        ]
        ap.set_pixels(Bol)
        time.sleep(8)
        ap.show_message("Hola usted esta volando sobre Bolivia", text_colour=[255, 255, 200])


        
            
        
         
    ###italy###
    elif (lati[0] <= 46 and lati[0] >= 37) and (longt[0] >= 7 and longt[0] <= 20):    
        print "ITALY"

        X = [255, 0, 0]  # Red 
        O = [255, 255, 255]  # White
        G = [0,225,0] # GREEN 
        italy = [ 
        G, G, G, O, O, X, X, X, 
        G, G, G, O, O, X, X, X, 
        G, G, G, O, O, X, X, X, 
        G, G, G, O, O, X, X, X,
        G, G, G, O, O, X, X, X, 
        G, G, G, O, O, X, X, X, 
        G, G, G, O, O, X, X, X, 
        G, G, G, O, O, X, X, X
        ] 
        ap.set_pixels(italy)
        time.sleep(8)
        ap.show_message("Ciao Tim vostra su Italia scommeto cho desidra si  puo", text_colour=[255, 180, 200]) 

    ###CROATIA##
    elif (lati[0] <= 45 and lati[0] >= 42) and (longt[0] >= 13 and longt[0] <= 17):    
        print "CROATIA"
        R = [255,0,0]  #RED
        W = [255,255,255] #WHITE
        B = [0, 0, 255] #BLUE

        CRO = [ 
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        W,W,W,W,W,W,W,W,
        W,W,W,R,R,W,W,W,
        W,W,W,W,W,W,W,W,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        ]
        ap.set_pixels(CRO)
        time.sleep(8)
        ap.show_message("Pozdrav od Croatia,", text_colour=[90, 255, 200])


    ###CROATIA##
    elif (lati[0] <= 46 and lati[0] >= 44) and (longt[0] >= 16 and longt[0] <= 19):    
        print "CROATIA"
        R = [255,0,0]  #RED
        W = [255,255,255] #WHITE
        B = [0, 0, 255] #BLUE

        CRO = [ 
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        W,W,W,W,W,W,W,W,
        W,W,W,R,R,W,W,W,
        W,W,W,W,W,W,W,W,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        ]
        ap.set_pixels(CRO)
        time.sleep(8)
        ap.show_message("Pozdrav od Croatia,", text_colour=[90, 255, 200])
        



    ####HUNGRY 
    elif (lati[0] <= 47 and lati[0] >= 46) and (longt[0] >= 17 and longt[0] <= 21):    
        print "HUNGRY"
        
        O =  [255, 255, 255] #white
        X = [255, 0, 0] #RED
        T = [0, 255, 0] #green

        Hungry = [ 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O, 
        T, T, T, T, T, T, T, T, 
        T, T, T, T, T, T, T, T, 
        T, T, T, T, T, T, T, T, 
        ]
        ap.set_pixels(Hungry)
        time.sleep(6)
        ap.show_message("Ha nem eszik ugy erezheti ezt!!", text_colour=[255, 255, 140])
        


    ###ROMAINIA
    elif (lati[0] <= 47 and lati[0] >= 43) and (longt[0] >= 22 and longt[0] <= 28):    
        print "ROMANIA"
        X = [0, 0, 255]  #blue    
        O = [255, 240, 10]  # Yellow  
        T = [255, 0, 0,] # red 

        Romania = [  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        X, X, X, O, O, T, T, T,  
        ]
        ap.set_pixels(Romania)
        time.sleep(6)
        ap.show_message("Salut la Jeff, ISS ", text_colour=[90, 255, 140])
        
        
        

        

    ###EGYPT###   USE THIS ONE ####
    elif (lati[0] <= 31 and lati[0] >= 22) and (longt[0] >= 22 and longt[0] <= 33):    
        print "EGYPT"

        X = [0,0,0]  # black
        O = [255,0,0]  # red
        Z = [255, 247, 0] #Yellow
        W=[255,255,255] #white
        question_mark = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        W, W, W, W, W, W, W, W,
        W, W, W, Z, Z, W, W, W,
        W, W, W, Z, Z, W, W, W,
        W, W, W, W, W, W, W, W,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]

        ap.set_pixels(question_mark)
        time.sleep(6)
        ap.show_message("You are flying over the Triangle Capital?", text_colour=[255, 255, 255])

    ###INDIA###   USE THIS ONE ####
    elif (lati[0] >= 6 and lati[0] <= 31) and (longt[0] >= 68 and longt[0] <= 86):    
        print "INDIA"

        x = [255,145,0]  # Orange
        w=[255,255,255] #White
        o = [0, 255,100] #Green
        k = [0, 0, 155]  # Blue
        iNDIA = [
        x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x,
        w, w, w, w, w ,w, w, w,
        w, w, w, k, k, w, w, w,
        w, w, w, k, k, w, w, w,
        w, w, w, w, w ,w, w, w,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        ]

        ap.set_pixels(iNDIA)
        time.sleep(6)
        ap.show_message("Kita turun dibawah, Halo ISS India", text_colour=[255, 255, 255])

    ###Venizwala###
    elif (lati[0] >= 3 and lati[0] <= 10) and (longt[0] >= -72 and longt[0] <= -63):    
        print "Venezuela"
        X = [255, 0, 0]  # Red  
        O = [255, 240, 10]  # Yellow
        L = [0, 255, 0] #BLUE
        P =[255, 255, 255] #WHITE 
         

        vEN = [ 
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O, 
        L, L, P, P, P, P, L, L, 
        L, P, L, L, L, L, P, L, 
        X, X,X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        X, X, X, X, X, X, X, X, 
        ] 
        ap.set_pixels(vEN) 

    ###PAKASTAIN###
    elif (lati[0] <= 25 and lati[0] >= 32) and (longt[0] >= 65 and longt[0] <= 75):    
        print "PAKASTAIN"

        X = [131, 84, 40]  # Dark Green 
        O = [255, 255, 255]  # White 
        Pakistain = [ 
        O, O, X, X, X, X, X, X, 
        O, O, X, X, O, X, X, X, 
        O, O, X, O, X, X, O, X, 
        O, O, X, O, X, X, X, X, 
        O, O, X, O, X, X, O, X, 
        O, O, X, X, O, O, X, X, 
        O, O, X, X, X, X, X, X, 
        O, O, X, X, X, X, X, X, 
        ] 
        ap.set_pixels(Pakistain)
        time.sleep(6)
        ap.show_message("Hello Tim. How are you on this fine day?", text_colour=[255, 255, 255]) 

    else:
        ap.show_message("Temperature: %s C" % temp[0:4], scroll_speed=(0.05))
        FLASH = 5000

        while FLASH > 0:   
            x = randint(0, 7)
            y = randint(0, 7)
            r = randint(0, 0)
            g = randint(0, 100)
            b = randint(0, 255)
            ap.set_pixel(x, y, r, g, b)
            FLASH = FLASH - 1

        ap.show_message("Checking Location", scroll_speed=(0.05))
                    
        ap.show_message("Pressure: %s Milibars" %pressure[0:5], scroll_speed=(0.05), text_colour=[255, 102, 204])
        FLASH = 5000

        while FLASH > 0:   
            x = randint(0, 7)
            y = randint(0, 7)
            r = randint(0, 0)
            g = randint(0, 255)
            b = randint(0, 100)
            ap.set_pixel(x, y, r, g, b)
            FLASH = FLASH - 1
            

        ap.show_message("Checking Location", scroll_speed=(0.05), text_colour=[0, 240, 0])       

           
       
      
  
   

   
    

   
 



