import pygame
import os
pygame.font.init()
pygame.mixer.init()
from classes import *

bg_width, bg_height = 1440, 790
win = pygame.display.set_mode((bg_width, bg_height))
pygame.display.set_caption("Capture the Flag!") 

white = (255, 255, 255)
black = (0, 0, 0)

fps = 60

spaceship_width, spaceship_height = 40, 55

ky_flag_taken = pygame.USEREVENT + 3
nj_flag_taken = pygame.USEREVENT + 4

border = pygame.Rect(bg_width//2 - 5, 0, 10, bg_height)

# bullet_hit_sound = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))

winner_font = pygame.font.SysFont('comicsans', 100)

yellow_spaceship_img = pygame.image.load(os.path.join('Assets', yellow_spaceship.image))
yellow_spaceship_img = pygame.transform.rotate(yellow_spaceship_img, 90)
yellow_spaceship_img = pygame.transform.scale(yellow_spaceship_img, (yellow_spaceship.width, yellow_spaceship.height))

red_spaceship_img = pygame.image.load(os.path.join('Assets', red_spaceship.image))
red_spaceship_img = pygame.transform.rotate(red_spaceship_img, 270)
red_spaceship_img = pygame.transform.scale(red_spaceship_img, (red_spaceship.width, red_spaceship.height))

ky_flag_img_1 = pygame.image.load(os.path.join('Assets', ky_flag_1.image))
ky_flag_img_1 = pygame.transform.scale(ky_flag_img_1, (ky_flag_1.width, ky_flag_1.height))
ky_flag_img_2 = pygame.image.load(os.path.join('Assets', ky_flag_2.image))
ky_flag_img_2 = pygame.transform.scale(ky_flag_img_2, (ky_flag_2.width, ky_flag_2.height))

nj_flag_img_1 = pygame.image.load(os.path.join('Assets', nj_flag_1.image))
nj_flag_img_1 = pygame.transform.scale(nj_flag_img_1, (nj_flag_1.width, nj_flag_1.height))
nj_flag_img_2 = pygame.image.load(os.path.join('Assets', nj_flag_2.image))
nj_flag_img_2 = pygame.transform.scale(nj_flag_img_2, (nj_flag_2.width, nj_flag_2.height))

space_bg = pygame.image.load(os.path.join('Assets', 'space.png'))
space_bg = pygame.transform.scale(space_bg, (bg_width, bg_height))  

def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= yellow_spaceship.speed
    if keys_pressed[pygame.K_d] and yellow.x + yellow.width < bg_width:
        yellow.x += yellow_spaceship.speed
    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= yellow_spaceship.speed
    if keys_pressed[pygame.K_s] and yellow.y + yellow.height < bg_height:
        yellow.y += yellow_spaceship.speed

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x > 0:
        red.x -= red_spaceship.speed
    if keys_pressed[pygame.K_RIGHT] and red.x + 40 < bg_width:
        red.x += red_spaceship.speed
    if keys_pressed[pygame.K_UP] and red.y > 0:
        red.y -= red_spaceship.speed
    if keys_pressed[pygame.K_DOWN] and red.y + 55 < bg_height:
        red.y += red_spaceship.speed

def red_ship_reset(red):
    red.x = bg_width - 150 - spaceship_height
    red.y = bg_height//2 - red_spaceship.width//2

def yellow_ship_reset(yellow):
    yellow.x = 150
    yellow.y = bg_height//2 - yellow_spaceship.width//2

def draw_winner(text):
    draw_text = winner_font.render(text, 1, white)
    win.blit(draw_text, (bg_width/2 - draw_text.get_width()/2, height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


def draw_window(red, yellow, ky_flag_capt_1, nj_flag_capt_1, ky_flag_drop_1, nj_flag_drop_1, 
            ky_flag_dropped_1, nj_flag_dropped_1, ky_flag_capt_2, nj_flag_capt_2, ky_flag_drop_2, nj_flag_drop_2, 
            ky_flag_dropped_2, nj_flag_dropped_2):

    global counter

    win.blit(space_bg, (0,0))
    pygame.draw.rect(win, black, border)

    if nj_flag_capt_1 == True:
        nj_flag_rect_1.x = red.x - nj_flag_1.width # flag.x = ship.x
        nj_flag_rect_1.y = red.y + 8
    elif nj_flag_drop_1 == True:
        global nj_drop_x_1
        nj_drop_x_1 = red.x - nj_flag_1.width # drop.x = ship.x
        nj_flag_rect_1.x = nj_drop_x_1 # flag.x = drop.x
        global nj_drop_y_1
        nj_drop_y_1 = red.y + 8
        nj_flag_rect_1.y = nj_drop_y_1
    elif nj_flag_dropped_1 == True:
        nj_flag_rect_1.x = nj_drop_x_1 # flag.x = drop.x
        nj_flag_rect_1.y = nj_drop_y_1

    if nj_flag_capt_2 == True:
        nj_flag_rect_2.x = red.x - nj_flag_2.width
        nj_flag_rect_2.y = red.y + 8
    elif nj_flag_drop_2 == True:
        global nj_drop_x_2
        nj_drop_x_2 = red.x - nj_flag_2.width
        nj_flag_rect_2.x = nj_drop_x_2
        global nj_drop_y_2
        nj_drop_y_2 = red.y + 8
        nj_flag_rect_2.y = nj_drop_y_2
    elif nj_flag_dropped_2 == True:
        nj_flag_rect_2.x = nj_drop_x_2
        nj_flag_rect_2.y = nj_drop_y_2

    if ky_flag_capt_1 == True:
        ky_flag_rect_1.x = yellow.x + yellow_spaceship.width
        ky_flag_rect_1.y = yellow.y + 8
    elif ky_flag_drop_1 == True:
        global ky_drop_x_1
        ky_drop_x_1 = yellow.x + yellow_spaceship.width
        ky_flag_rect_1.x = ky_drop_x_1
        global ky_drop_y_1
        ky_drop_y_1 = yellow.y + 8
        ky_flag_rect_1.y = ky_drop_y_1
    elif ky_flag_dropped_1 == True:
        ky_flag_rect_1.x = ky_drop_x_1
        ky_flag_rect_1.y = ky_drop_y_1

    if ky_flag_capt_2 == True:
        ky_flag_rect_2.x = yellow.x + ky_flag_2.width
        ky_flag_rect_2.y = yellow.y + 8
    elif ky_flag_drop_2 == True:
        global ky_drop_x_2
        ky_drop_x_2 = yellow.x + ky_flag_2.width
        ky_flag_rect_2.x = ky_drop_x_2
        global ky_drop_y_2
        ky_drop_y_2 = yellow.y + 8
        ky_flag_rect_2.y = ky_drop_y_2
    elif ky_flag_dropped_2 == True:
        ky_flag_rect_2.x = ky_drop_x_2
        ky_flag_rect_2.y = ky_drop_y_2

    win.blit(ky_flag_img_1, (ky_flag_rect_1.x, ky_flag_rect_1.y))
    win.blit(nj_flag_img_1, (nj_flag_rect_1.x, nj_flag_rect_1.y))
    win.blit(ky_flag_img_2, (ky_flag_rect_2.x, ky_flag_rect_2.y))
    win.blit(nj_flag_img_2, (nj_flag_rect_2.x, nj_flag_rect_2.y))

    win.blit(yellow_spaceship_img, (yellow.x, yellow.y))
    win.blit(red_spaceship_img, (red.x, red.y))

    pygame.display.update()


def main():

    global counter

    red = pygame.Rect(bg_width - 150 - spaceship_height, bg_height//2 - red_spaceship.width//2, red_spaceship.width, spaceship_height)
    yellow = pygame.Rect(150, bg_height//2 - spaceship_width//2, spaceship_width, spaceship_height)

    global ky_flag_rect_1
    global ky_flag_rect_2
    global nj_flag_rect_1
    global nj_flag_rect_2

    ky_flag_rect_1 = pygame.Rect(red.x + spaceship_width, 50, spaceship_height, spaceship_width)
    ky_flag_rect_2 = pygame.Rect(red.x + spaceship_width, bg_height - 50, spaceship_height, spaceship_width)
    nj_flag_rect_1 = pygame.Rect(yellow.x - spaceship_height, 50, spaceship_height, spaceship_width)
    nj_flag_rect_2 = pygame.Rect(yellow.x - spaceship_height, bg_height - 50, spaceship_height, spaceship_width)

    ky_flag_capt_1 = False
    ky_flag_capt_2 = False
    nj_flag_capt_1 = False
    nj_flag_capt_2 = False
    ky_flag_drop_1 = False
    ky_flag_drop_2 = False
    nj_flag_drop_1 = False
    nj_flag_drop_2 = False
    ky_flag_dropped_1 = False
    ky_flag_dropped_2 = False
    nj_flag_dropped_1 = False
    nj_flag_dropped_2 = False

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()  

        if red.x < border.x:
            red_spaceship.vulnerable = True
        else:
            red_spaceship.vulnerable = False

        if yellow.x + yellow.width > border.x + border.width:
            yellow_spaceship.vulnerable = True
        else:
            yellow_spaceship.vulnerable = False  

        if nj_flag_dropped_1 == True:
            nj_flag_dropped_1 = False
            red_ship_reset(red) # red ship reset

        if nj_flag_dropped_2 == True:
            nj_flag_dropped_2 = False
            red_ship_reset(red) # red ship reset

        if ky_flag_dropped_1 == True:
            ky_flag_dropped_1 = False
            yellow_ship_reset(yellow) # red ship reset

        if ky_flag_dropped_2 == True:
            ky_flag_dropped_2 = False
            yellow_ship_reset(yellow) # red ship reset

        if nj_flag_drop_1 == True: 
            nj_flag_dropped_1 = True # dropped = true
            nj_flag_drop_1 = False # drop = false

        if nj_flag_drop_2 == True: 
            nj_flag_dropped_2 = True # dropped = true
            nj_flag_drop_2 = False # drop = false

        if ky_flag_drop_1 == True: 
            ky_flag_dropped_1 = True # dropped = true
            ky_flag_drop_1 = False # drop = false

        if ky_flag_drop_2 == True: 
            ky_flag_dropped_2 = True # dropped = true
            ky_flag_drop_2 = False # drop = false

        if red.colliderect(nj_flag_rect_1): # red collide flag
            nj_flag_capt_1 = True   # capt = true

        if red.colliderect(nj_flag_rect_2):
            nj_flag_capt_2 = True  

        if yellow.colliderect(ky_flag_rect_1):
            ky_flag_capt_1 = True

        if yellow.colliderect(ky_flag_rect_2):
            ky_flag_capt_2 = True

        if red.colliderect(yellow) and red_spaceship.vulnerable: # red collide yellow
            if nj_flag_capt_1 == True:
                nj_flag_capt_1 = False # capt = false
                nj_flag_drop_1 = True # drop = true
            if nj_flag_capt_2 == True:
                nj_flag_drop_2 = True
                nj_flag_capt_2 = False
            elif nj_flag_dropped_1 and nj_flag_capt_1 == True:
                nj_flag_dropped_1 = False
            elif nj_flag_dropped_2 and nj_flag_capt_2 == True:
                nj_flag_dropped_2 = False
            elif nj_flag_capt_1 == False and nj_flag_drop_1 == False:
                red_ship_reset(red)

        if yellow.colliderect(red) and yellow_spaceship.vulnerable:
            if ky_flag_capt_1 == True:
                ky_flag_capt_1 = False # capt = false
                ky_flag_drop_1 = True # drop = true
            if ky_flag_capt_2 == True:
                ky_flag_drop_2 = True
                ky_flag_capt_2 = False
            elif ky_flag_dropped_1 and ky_flag_capt_1 == True:
                ky_flag_dropped_1 = False
            elif ky_flag_dropped_2 and ky_flag_capt_2 == True:
                ky_flag_dropped_2 = False
            elif ky_flag_capt_1 == False and ky_flag_drop_1 == False:
                yellow_ship_reset(yellow)

        draw_window(red, yellow, ky_flag_capt_1, nj_flag_capt_1, ky_flag_drop_1, nj_flag_drop_1, 
            ky_flag_dropped_1, nj_flag_dropped_1, ky_flag_capt_2, nj_flag_capt_2, ky_flag_drop_2, nj_flag_drop_2, 
            ky_flag_dropped_2, nj_flag_dropped_2)

        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)

        winner_text = ''
        if nj_flag_rect_1.x > border.x + border.width:
            winner_text = 'RED WINS!'
        if ky_flag_rect_1.x + ky_flag_rect_1.width < border.x:
            winner_text = 'YELLOW WINS!'
        if nj_flag_rect_2.x > border.x + border.width:
            winner_text = 'RED WINS!'
        if ky_flag_rect_2.x + ky_flag_rect_2.width < border.x:
            winner_text = 'YELLOW WINS!'
        if winner_text != '':
            draw_winner(winner_text)
            break

        if keys_pressed[pygame.K_x]:
            pygame.quit()
        if keys_pressed[pygame.K_t]:
            main()

    main()

if __name__ == "__main__":
    main()



