#Создай собственный Шутер!
from random import *
from pygame import *

window = display.set_mode((1000, 650))
display.set_caption('Лапиринд')
background = transform.scale(image.load("galaxy.jpg"), (1000, 650))

finish = False

clock = time.Clock()
FPS = 15

class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y, spid):
        super().__init__()
        self.image = transform.scale(image.load(image1), (70, 70))
        self.speed = spid
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 950:
            self.rect.x += self.speed
    def fire(self):
        bulet = Bulet("obresan.png",self.rect.centerx,self.rect.top,10)
        bulets.add (bulet)
        
            
        
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >700:
            self.rect.y = -50
            self.rect.x =  randint (0,700)
            self.speed = randint(2,5)


class Bulet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <0:
            self.kill()



font.init()
font = font.SysFont("Arial", 140)
gameover = font.render('GAME OVER', True, (255, 0, 0))
youwin = font.render('U WIN', True, (0, 255, 0))

mixer.init()
mixer.music.load("gta.mp3")
mixer.music.play()

bulets = sprite.Group()

hero = Player("putin.png", 400,460, 15)
p = sprite.Group()
for i in range(185):

    cyborg = Enemy("ave.png", randint (0,700), -40, randint(2,5))

    p.add(cyborg)

game = True
while game:
    
    clock.tick(FPS)
    if finish != True:
        window.blit(background, (0, 0))
        hero.reset()    
        hero.update()
        p.update()
        p.draw(window)
        bulets.update()
        bulets.draw(window)

    jhr = sprite.groupcollide(bulets,p,True,True)   
    for g in jhr:
        cyborg = Enemy("ave.png", randint (0,700), -40, randint(2,5))

        p.add(cyborg)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type==KEYDOWN:
            if e.key== K_SPACE:
                hero.fire()

        

    display.update()
    