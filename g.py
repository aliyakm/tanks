import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/bg.jfif')

#bg sound
mixer.music.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/bgsound.mp3')
mixer.music.play(-1)

done = False
playerImage = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/playerright.png')
playerleft = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/playerleft.png')
playerright = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/playerright.png')
playerdown = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/playerdown.png')
playerup = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/playerup.png')

player2Image = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/2playerright.png')
player2left = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/2playerleft.png')
player2right = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/2playerright.png')
player2down = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/2playerdown.png')
player2up = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/2playerup.png')

bulletImage = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/bulletright.png')
bulletup = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/bulletup.png')
bulletdown = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/bulletdown.png')
bulletright = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/bulletright.png')
bulletleft = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/bulletleft.png')

bullet2Image = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/ebulletright.png')
bullet2up = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/ebulletup.png')
bullet2down = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/ebulletdown.png')
bullet2right = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/ebulletright.png')
bullet2left = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/ebulletleft.png')

h3Image = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/h3.png')
h2Image = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/h2.png')
h1Image = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/h1.png')
h0Image = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/h0.png')

gameover = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/tanks/gg.png')

#Player1
d = 5
player_x = 400
player_y = 268
player_dx = 5
player_dy = 0

def player(x, y):
    screen.blit(playerImage, (x, y))

#Player2
player2_x = 300
player2_y = 268
player2_dx = 5
player2_dy = 0

def player2(x, y):
    screen.blit(player2Image, (x, y))

#Bullet
d2 = 15
bullet_x = 0
bullet_y = 50
bullet_dy = 8
bullet_dx = 8
bullet_state = "ready" 
def fire_bullet(bullet_x, bullet_y, player_x, player_y):
    global bullet_state
    bullet_state = "fire"
    if playerImage is playerup:
        screen.blit(bulletup, (bullet_x+28, bullet_y-40))
    if playerImage is playerdown:
        screen.blit(bulletdown, (bullet_x+28, bullet_y+70))
    if playerImage is playerright:
        screen.blit(bulletright, (bullet_x+70, bullet_y+22))
    if playerImage is playerleft:
        screen.blit(bulletleft, (bullet_x-40, bullet_y+22))
#Bullet2
bullet2_x = 0
bullet2_y = 50
bullet2_dy = 8
bullet2_dx = 8
bullet2_state = "ready"
def fire_bullet2(bullet_x, bullet_y):
    global bullet2_state
    bullet2_state = "fire"
    if player2Image is player2up:
        screen.blit(bullet2up, (bullet_x+28, bullet_y-40))
    if player2Image is player2down:
        screen.blit(bullet2down, (bullet_x+28, bullet_y+70))
    if player2Image is player2right:
        screen.blit(bullet2right, (bullet_x+70, bullet_y+22))
    if player2Image is player2left:
        screen.blit(bullet2left, (bullet_x-40, bullet_y+22))

#Text
font = pygame.font.SysFont(None, 35)
top1_x = 10
top1_y = 10
def playertop1(x, y):
    playertop = font.render("PLAYER 2", True, (255, 255, 255))
    screen.blit(playertop, (x, y))

top2_x = 675
top2_y = 10
def playertop2(x, y):
    playertop = font.render("PLAYER 1", True, (255, 255, 255))
    screen.blit(playertop, (x, y))
#hearts
def heart(x, y, score):
    screen.blit(h3Image, (x, y))
    if score == 1:
        screen.blit(h2Image, (x, y))
    if score == 2:
        screen.blit(h1Image, (x, y))
    if score >= 3:
        screen.blit(h0Image, (x, y))

def isCollided1(player_x, player_y, bullet2_x, bullet2_y):
    #distance
    d = math.sqrt((math.pow(player_x - bullet2_x,2)) + (math.pow(player_y - bullet2_y,2)))
    if d < 50:
        return True
    else:
        return False

#scores
score1 = 0
score2 = 0

FPS = 30

clock = pygame.time.Clock()

while not done:
    mill = clock.tick(FPS)
    screen.fill((135, 100, 46))
    screen.blit(background, (0, 0))
    
    player(player_x, player_y)
    #player move
    player_x += player_dx
    player_y += player_dy
    
    player2(player2_x, player2_y)
    #player2 move
    player2_x += player2_dx
    player2_y += player2_dy

    playertop1(top1_x, top1_y)
    playertop2(top2_x, top2_y)

    heart(5, 35, score1)
    heart(650, 35, score2)

    for event in pygame.event.get():
        #event on quit
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: player_dx = -d; player_dy = 0; playerImage = playerleft
    if pressed[pygame.K_RIGHT]: player_dx = d; player_dy = 0; playerImage = playerright
    if pressed[pygame.K_UP]: player_dy = -d; player_dx = 0; playerImage = playerup
    if pressed[pygame.K_DOWN]: player_dy = d; player_dx = 0; playerImage = playerdown
    if pressed[pygame.K_RETURN]: 
        if bullet_state == "ready":
            bullet1_sound = mixer.Sound('bull2.wav')
            bullet1_sound.play()
            bulletx = player_x; bullety = player_y
            bullet_x = bulletx; bullet_y = bullety
            fire_bullet(bullet_x, bullet_y, player_x, player_y)
    if pressed[pygame.K_a]: player2_dx = -d; player2_dy = 0; player2Image = player2left
    if pressed[pygame.K_d]: player2_dx = d; player2_dy = 0; player2Image = player2right
    if pressed[pygame.K_w]: player2_dy = -d; player2_dx = 0; player2Image = player2up
    if pressed[pygame.K_s]: player2_dy = d; player2_dx = 0; player2Image = player2down
    if pressed[pygame.K_SPACE]: 
        if bullet2_state == "ready":
            bullet1_sound = mixer.Sound('bull2.wav')
            bullet1_sound.play()
            bullet2x = player2_x; bullet2y = player2_y
            bullet2_x = bullet2x; bullet2_y = bullet2y
            fire_bullet2(bullet2_x, bullet2_y)
    
    #Bullet 1 moves
    if bullet_y<0 or bullet_y>600 or bullet_x<0 or bullet_x>800:
        bullet_y = player_y
        bullet_state = "ready"
    #Bullet 2 moves
    if bullet2_y<0 or bullet2_y>600 or bullet2_x<0 or bullet2_x>800:
        bullet2_y = player2_y
        bullet2_state = "ready"
    #bullet 1
    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y, player_x, player_y)
        if playerImage is playerup: bullet_dy = -d2; bullet_y += bullet_dy; bulletImage = bulletup
        if playerImage is playerdown: bullet_dy = d2; bullet_y += bullet_dy; bulletImage = bulletdown
        if playerImage is playerright: bullet_dx = d2; bullet_x += bullet_dx; bulletImage = bulletright
        if playerImage is playerleft: bullet_dx = -d2; bullet_x += bullet_dx; bulletImage = bulletleft
    #bullet 2 
    if bullet2_state is "fire":
        fire_bullet2(bullet2_x, bullet2_y)
        if player2Image is player2up: bullet2_dy = -d2; bullet2_y += bullet2_dy; bulletImage = bulletup
        if player2Image is player2down: bullet2_dy = d2; bullet2_y += bullet2_dy; bulletImage = bulletdown
        if player2Image is player2right: bullet2_dx = d2; bullet2_x += bullet2_dx; bulletImage = bulletright
        if player2Image is player2left: bullet2_dx = -d2; bullet2_x += bullet2_dx; bulletImage = bulletleft

    if player_x > 805:
        player_x = 0
    if player_x < 0:
        player_x = 800
    if player_y > 600:
        player_y = 0
    if player_y < 0:
        player_y = 600

    if player2_x > 805:
        player2_x = 0
    if player2_x < 0:
        player2_x = 800
    if player2_y > 600:
        player2_y = 0
    if player2_y < 0:
        player2_y = 600

    #collision between player 1 and bullet 2
    coll1 = isCollided1(player_x, player_y, bullet2_x, bullet2_y)
    if coll1:
        expl_sound = mixer.Sound('explo1.wav')
        expl_sound.play()
        bullet2_x = player2_x
        bullet2_y = player2_y
        bullet2_state = "ready"
        score2 += 1
                    
    #collision between player 2 and bullet 1
    coll2 = isCollided1(player2_x, player2_y, bullet_x, bullet_y)
    if coll2:
        expl_sound = mixer.Sound('explo1.wav')
        expl_sound.play()
        bullet_x = player_x
        bullet_y = player_y
        bullet_state = "ready"
        score1 += 1
        
    if score1 >= 3:
        screen.blit(gameover, (270, 160))
        win_sound = mixer.Sound('win.wav')
        win_sound.play(1)
        text1 = font.render("PLAYER 1 IS WINNER", True, (255, 255, 255))
        screen.blit(text1, (270, 420))
        player_dx = 0
        player_dy = 0
        player2_dx = 0
        player2_dy = 0

    if score2 >= 3:
        screen.blit(gameover, (270, 160))
        win_sound = mixer.Sound('win.wav')
        win_sound.play(1)
        text2 = font.render("PLAYER 2 IS WINNER", True, (255, 255, 255))
        screen.blit(text2, (270, 420))
        player_dx = 0
        player_dy = 0
        player2_dx = 0
        player2_dy = 0

    pygame.display.flip()