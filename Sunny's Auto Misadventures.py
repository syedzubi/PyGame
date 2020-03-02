
import pygame,sys
import time
import random
pygame.init()

display_width=800
display_height=700

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)

bright_red = (255,0,0)
bright_green = (0,255,0)


car_width = 100


car_height = 150


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Sunny's Auto Misadventure")
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
BG= pygame.image.load("background.png")

pause = False

def things_dodged(count):
    font = pygame.font.Font(None, 25)
    text = font.render("Score:"+str(count), True, green)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx,thingy, thingw, thingh])
    

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface= font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

    
def Background():
    gameDisplay.blit(BG,(0,0))
    

def crash():
    
   
    pygame.mixer.music.load('crash.mp3')
    pygame.mixer.music.play(0)
    message_display("You Crashed")
  
    
def button(msg,x,y,w,h,ic,ac,action=None):

         mouse = pygame.mouse.get_pos()
         click = pygame.mouse.get_pressed()
         if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                if action == "play":
                    game_loop()
                    
                elif action == "quit":
                    pygame.quit()
                    quit()
                    
                    
         else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

         smallText = pygame.font.Font("freesansbold.ttf",20)
         textSurf, textRect = text_objects(msg,smallText)
         textRect.center = ( (x+(w/2)),(y+(h/2)) )
         gameDisplay.blit(textSurf, textRect)

def unpause():
    pause = False
    game_loop()

def paused():

     while pause:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
         gameDisplay.fill(white)

         largeText = pygame.font.Font('freesansbold.ttf',50)
         TextSurf, TextRect = text_objects("Paused", largeText)
         TextRect.center = ((display_width/2),(display_height/2))
         gameDisplay.blit(TextSurf,TextRect)

         button("Resume",150,450,100,50,green,bright_green,unpause)
         button("QUIT",550,450,100,50,red,bright_red,"quit")    

         pygame.display.update()
         clock.tick(15)      

def game_intro():

     intro = True

     while intro:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
         gameDisplay.fill(white)
         largeText = pygame.font.Font('freesansbold.ttf',50)
         TextSurf, TextRect = text_objects("Sunny's Misadventures: Infiniti", largeText)
         TextRect.center = ((display_width/2),(display_height/2))
         gameDisplay.blit(TextSurf,TextRect)

         button("GO!",150,450,100,50,green,bright_green,"play")
         button("QUIT",550,450,100,50,red,bright_red,"quit")

         pygame.display.update()
         clock.tick(15)    
           
           
def game_loop():
    global pause
    

    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play(-1)
    x=(display_width * 0.442)
    y=(display_height * 0.75)
    x_change=0
    y_change=0
    thing_startx= random.randrange(0, display_width)
    thing_starty= -600
    thing_speed= 7
    thing_width= 100
    thing_height= 100
    dodged = 0



    gameExit = False

    while not gameExit :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            
                if event.key == pygame.K_p:
                    pause = True
                    paused()




            if event.type==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


        x += x_change
        y += y_change
                    
        

        gameDisplay.fill(white)
        Background()

        
        car(x,y)

        things_dodged(dodged)
        

        if x > display_width - car_width or x < 0:
           crash()
           

        if y > display_height - car_height or y < 0:
            crash()
            
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx= random.randrange(0,display_width)
            dodged += 1
            thing_speed += 0.5
            

        things(thing_startx, thing_starty, thing_width,thing_height,black)
        thing_starty += thing_speed




        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                crash()




        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()

