
import pygame
from pygame.locals import *
import sys, random
#python uses pip to manage your gamespythpo
#to run the program, use python3 doodle.py (vs code only)
#python3 doodle.py

pygame.init() #this initializaes all modules in python
vec = pygame.math.Vector2 #2 4 two dimensional
#vectors are a pair of numbers together
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
HARD = 9
class Player(pygame.sprite.Sprite):
     	
     #pygame.sprite.spritecollide(sprite, sprite_group, delete) #syntax of sprite collide
     def __init__(self):
          super().__init__()#Initalizes the base Sprite Class.
          self.surf = pygame.Surface((30, 30))
          self.surf.fill((128,255,40))
          self.rect = self.surf.get_rect()

          self.pos = vec((10, 385))
          self.vel = vec(0,0)
          self.acc = vec(0,0)
          #vec creates variables in two dimensions
          #when we initialized it, itll start creating vectors
          #veloity and acceleration are vector qualities.
          
          self.surf = pygame.Surface((30, 30)) 
          self.surf.fill((128,255,40))
          self.rect = self.surf.get_rect(center = (10, 420)) 
          self.jump_count = 0  # Tracks jumps made since last landing

     def move(self):
          #The function first re-sets the value of the acceleration to 0, then checks for key presses. 
          self.acc = vec(0,1)
          pressed_keys = pygame.key.get_pressed()
            
          if pressed_keys[K_LEFT]:
               self.acc.x = -ACC
          if pressed_keys[K_RIGHT]:
               self.acc.x = ACC     
               # If the left key has been pressed, it will update the acceleration with a negative value (acceleration in the opposite direction). If the right key has been pressed, acceleration will have a positive value.
          self.acc.x += self.vel.x * FRIC
          self.vel += self.acc
          self.pos += self.vel + 0.5 * self.acc
          #THis is an equation of motion on the third line
          #Also uses friction to decrease the value of velocity
          #Without friction, player will not accelerate
          if self.pos.x > WIDTH:
               self.pos.x = 0
          if self.pos.x < 0:
               self.pos.x = WIDTH  

          self.rect.midbottom = self.pos
     def update(self):
          hits = pygame.sprite.spritecollide(P1 , platforms, False)
          if P1.vel.y > 0 and hits:
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0
                    self.jump_count = 0  # Reset jumps when grounded

     

     def jump(self):
    # Check if the player is standing on a platform
      hits = pygame.sprite.spritecollide(self, platforms, False)
    # If they are on a platform (grounded), OR  They have jumped less than 2 times (double jump allowed)

      if hits or self.jump_count < 2:
               self.vel.y = -17.5 # Apply upward velocity (negative because y increases downward)
               self.jump_count += 1  # Track how many jumps have been made


def plat_gen():
    # Keep adding platforms until there are at least 7
         if len(platforms) < HARD :
        # Pick a random width for variety
               width = random.randrange(10, 15)
    #adjust the distance above platforms generated
          # Create a new platform
               p = platform()
               C = True
               # Set its position:
               # X is random but within screen bounds
               # Y is just above the screen (so it scrolls down naturally)
               
               if C:
                    p = platform()
                    p.rect.center = (
                         random.randrange(0, WIDTH - width),
                         random.randrange(-250, 0)
                    )
                    C = check(p, platforms)
               # Add the platform to both sprite groups
               if not C:
                    platforms.add(p)
                    all_sprites.add(p)   
def check(platform, groupies):
    """
    This function checks if the platform is bumping into or too close to others.
    
    platform: one platform we're checking
    groupies: a bunch of platforms or things
    """

    # Look to see if the platform is bumping into any others
    if pygame.sprite.spritecollideany(platform, groupies):
        return True

    # Look to see if the platform is very close (but not touching)
    for entity in groupies:
        if entity == platform:
            continue  # Skip if it's the same platform

        # If it's less than 50 steps away from the top or bottom, it's too close
        if (abs(platform.rect.top - entity.rect.bottom) < 50) and \
           (abs(platform.rect.bottom - entity.rect.top) < 50):
            return True

    return False  # Everything is okay

class platform(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          self.surf = pygame.Surface((100, 5))
          self.surf.fill((255,0,0))
          self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH-10), 
                                                   random.randint(0, HEIGHT-30)))
          
          

#create a blank game window the caption of a game
PT1 = platform()
PT1 = platform()
PT1.surf = pygame.Surface((WIDTH, 20))  # Create the surface first
PT1.surf.fill((255, 0, 0))              # Fill it with red
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))  # Now get the correct rect
P1 = Player()	

platforms = pygame.sprite.Group()
platforms.add(PT1)
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
#ygame.display.set_mode((600, 600))

# creating a bool value which checks
# if game is running
running = True

# Check for event if user has pushed
    # any event in queue

     # Check for event if user has pushed
    # any event in queue
    ##for event in pygame.event.get():
        
         # if event is of type quit then 
        # set running bool to false
        
for x in range(random.randint(6, 7)):
     pl = platform()
     platforms.add(pl)
     all_sprites.add(pl)


FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")
while running:
     for event in pygame.event.get():
        
         # if event is of type quit then 
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            #sys.exit()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                  P1.jump()
            #This is a way to do it
     if P1.rect.top <= HEIGHT / 2: #checks postion of player to allow it to understand if it needs to move up.
             P1.pos.y += abs(P1.vel.y) #this allows us to continously update the game and players screen
             for plat in platforms:
               plat.rect.y += abs(P1.vel.y)#We’ve updated every other sprite on the screen. iterate through all the platforms and update their position as well.
               if plat.rect.top >= HEIGHT:
                    plat.kill() #PYTHON'S speed is hot ass, so we need to delete this stuff to make it as simple as possible for our player to play without lag.
     displaysurface.fill((0,0,0))

     P1.move()
     P1.update()
     plat_gen()
     for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
 
     pygame.display.update()
     FramePerSec.tick(FPS)
               

pygame.time.get_ticks()
