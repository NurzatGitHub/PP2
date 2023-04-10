import pygame, sys
from pygame.locals import *
import random, time
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN = 0

font = pygame.font.SysFont("Verdana", 60)
font1 = pygame.font.SysFont("Verdana", 36)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load(r"C:\Users\Nurza\Documents\PP2\week8\1.racer\AnimatedStreet.png")
pygame.mixer.Sound(r"C:\Users\Nurza\Documents\PP2\week8\1.racer\background.wav").play(-1)
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Nurza\Documents\PP2\week8\1.racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Nurza\Documents\PP2\week8\1.racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
E1 = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E1)
P1 = Player()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Nurza\Documents\PP2\week8\1.racer\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width, SCREEN_HEIGHT-self.rect.width),0)
        
        while pygame.sprite.spritecollideany(self, enemies):
            self.rect.center = (random.randint(self.rect.width, SCREEN_HEIGHT-self.rect.width),0)
            
    def move(self):
        global COIN
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width, SCREEN_HEIGHT-self.rect.width),0)
        elif Collide():
            check_level(COIN)
            COIN += 1
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width, SCREEN_HEIGHT-self.rect.width),0)

C1 = Coin()
coins = pygame.sprite.Group()
coins.add(C1)

class Moneys(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Nurza\Documents\PP2\week9\1.racer\moneys.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width, 4*SCREEN_HEIGHT-self.rect.width),0)
        
        while pygame.sprite.spritecollideany(self, enemies) or pygame.sprite.spritecollideany(self,coins):
            self.rect.center = (random.randint(self.rect.width, 4*SCREEN_HEIGHT-self.rect.width),0)
            
    def move(self):
        global COIN
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width, 4*SCREEN_HEIGHT-self.rect.width),0)
        elif Collide():
            check_level(COIN)
            COIN += 10
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width, 4*SCREEN_HEIGHT-self.rect.width),0)
M1 = Moneys()
coins.add(M1)

class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Nurza\Documents\PP2\week9\1.racer\money.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width, 2*SCREEN_HEIGHT-self.rect.width),0)
        
        while pygame.sprite.spritecollideany(self, enemies) or pygame.sprite.spritecollideany(self,coins):
            self.rect.center = (random.randint(self.rect.width, 2*SCREEN_HEIGHT-self.rect.width),0)
            
    def move(self):
        global COIN
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width, 2*SCREEN_HEIGHT-self.rect.width),0)
        elif Collide():
            check_level(COIN)
            COIN += 5
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width, 2*SCREEN_HEIGHT-self.rect.width),0)
M2 = Money()
coins.add(M2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(M1)
all_sprites.add(M2)

def Collide():
    if pygame.sprite.spritecollideany(P1,coins):
        return True
    else:return False
def check_level(coin):
    global SPEED
    global LEVEL
    if coin >= 50:
        SPEED += 0.5
        
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    money = font1.render(str(COIN),True,(255, 234, 0))
    DISPLAYSURF.blit(background, (0,0))
    DISPLAYSURF.blit(money,(SCREEN_WIDTH/2,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r'C:\Users\Nurza\Documents\PP2\week8\1.racer\crash.wav').play()
        time.sleep(1)
                   
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    FramePerSec.tick(FPS)