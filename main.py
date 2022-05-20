import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jesus Game')
clock = pygame.time.Clock()

music = pygame.mixer.Sound('./data/audio/Ameno.wav')
music.play(loops = -1)

hit1 = pygame.mixer.Sound('./data/audio/Aced.wav')
hit2 = pygame.mixer.Sound('./data/audio/Crash.wav')
hit3 = pygame.mixer.Sound('./data/audio/McOof.wav')
hit4 = pygame.mixer.Sound('./data/audio/RbOof.wav')
hit5 = pygame.mixer.Sound('./data/audio/Wilhelm.wav')

def hit_sound():
    hitx = random.randint(1,5)

    if hitx == 1:
        hit1.play()
    elif hitx == 2:
        hit2.play()
    elif hitx == 3:
        hit3.play()
    elif hitx == 4:
        hit4.play()
    elif hitx == 5:
        hit5.play()

font = pygame.font.Font('./data/font/font.ttf', 45)
sm_font = pygame.font.Font('./data/font/font.ttf', 20)

background = pygame.Surface((800,600))
background.fill('DarkGrey')

c_surf = pygame.image.load('./data/graphics/Cross.png').convert_alpha()
c_rect = c_surf.get_rect(center = (400,300))

j_surf = pygame.image.load('./data/graphics/Jesus.png').convert_alpha()
j_rect = j_surf.get_rect(bottomright = (0,0))

b_surf = pygame.image.load('./data/graphics/Bucket.png').convert_alpha()
b_rect = b_surf.get_rect(bottomright = (0,0))

nf_surf = pygame.image.load('./data/graphics/NailFull.png').convert_alpha()
nf_rect = nf_surf.get_rect(bottomright = (0,0))

nh1_surf = pygame.image.load('./data/graphics/NailHead.png').convert_alpha()
nh2_surf = pygame.image.load('./data/graphics/NailHead.png').convert_alpha()
nh3_surf = pygame.image.load('./data/graphics/NailHead.png').convert_alpha()
nh4_surf = pygame.image.load('./data/graphics/NailHead.png').convert_alpha()
nh5_surf = pygame.image.load('./data/graphics/NailHead.png').convert_alpha()
nh1_rect = nh1_surf.get_rect(bottomright = (0,0))
nh2_rect = nh2_surf.get_rect(bottomright = (0,0))
nh3_rect = nh3_surf.get_rect(bottomright = (0,0))
nh4_rect = nh4_surf.get_rect(bottomright = (0,0))
nh5_rect = nh5_surf.get_rect(bottomright = (0,0))
n = 0
nail_count = 1

rotated_j_surf = pygame.transform.rotate(j_surf, 90).convert_alpha()
rotated_j_rect = rotated_j_surf.get_rect(midleft = (0,560))
x = 0

jc_surf = pygame.image.load('./data/graphics/JesusOnCross.png').convert_alpha()
jc_rect = jc_surf.get_rect(center = (400,300))

reset_surf = pygame.image.load('./data/graphics/Reset.png').convert_alpha()
reset_rect = reset_surf.get_rect(bottomright = (795,595))

text_place_surf = font.render('Place Jesus on the Cross', False, 'Black')
text_place_rect = text_place_surf.get_rect(center = (400,50))

text_nail_surf = font.render('Nail Jesus to the Cross', False, 'Black')
text_nail_rect = text_nail_surf.get_rect(center = (400,50))

text_label_surf = sm_font.render('NAILS', False, 'Red')
text_label_rect = text_label_surf.get_rect(midbottom = b_rect.midbottom)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background,(0,0))
    
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if j_rect.left > c_rect.left:
        if j_rect.right < c_rect.right:
            if j_rect.top > c_rect.top:
                if j_rect.bottom < c_rect.bottom:
                    if mouse_click == (False, False, False):
                        x = 2
                        j_rect.bottomright = (0,0)
                        rotated_j_rect.bottomright = (0,0)
                        c_rect.bottomright = (0,0)
                    else:
                        screen.blit(c_surf,c_rect)
                else:
                    screen.blit(c_surf,c_rect)
            else:
                screen.blit(c_surf,c_rect)
        else:
            screen.blit(c_surf,c_rect)
    else:
        screen.blit(c_surf,c_rect)

    if rotated_j_rect.collidepoint((mouse_pos)):
        if mouse_click == (True, False, False):
            j_rect.center = mouse_pos
            rotated_j_rect.center = mouse_pos
            x = 1

    if x == 0:
        screen.blit(text_place_surf,text_place_rect)
        screen.blit(rotated_j_surf,rotated_j_rect)
    elif x == 1:
        screen.blit(j_surf,j_rect)
        screen.blit(text_place_surf,text_place_rect)
    else:
        b_rect.bottomleft = (5,595)
        text_label_rect.midbottom = b_rect.midbottom
        screen.blit(jc_surf,jc_rect)
        screen.blit(b_surf,b_rect)
        screen.blit(text_nail_surf,text_nail_rect)
        screen.blit(text_label_surf,text_label_rect)

    if b_rect.collidepoint((mouse_pos)):
        if mouse_click == (True, False, False):
            n = 1

    screen.blit(nh1_surf,nh1_rect)
    screen.blit(nh2_surf,nh2_rect)
    screen.blit(nh3_surf,nh3_rect)
    screen.blit(nh4_surf,nh4_rect)
    screen.blit(nh5_surf,nh5_rect)

    if n == 1 and nail_count <= 5:
        nf_rect.midbottom = mouse_pos
        screen.blit(nf_surf,nf_rect)
        if jc_rect.collidepoint((mouse_pos)) and nail_count == 1:
            if mouse_click == (False, False, False):
                hit_sound()
                nh1_rect.midbottom = mouse_pos
                screen.blit(nh1_surf,nh1_rect)
                n = 0
                nail_count += 1
        elif jc_rect.collidepoint((mouse_pos)) and nail_count == 2:
            if mouse_click == (False, False, False):
                hit_sound()
                nh2_rect.midbottom = mouse_pos
                screen.blit(nh2_surf,nh2_rect)
                n = 0
                nail_count += 1
        elif jc_rect.collidepoint((mouse_pos)) and nail_count == 3:
            if mouse_click == (False, False, False):
                hit_sound()
                nh3_rect.midbottom = mouse_pos
                screen.blit(nh3_surf,nh3_rect)
                n = 0
                nail_count += 1
        elif jc_rect.collidepoint((mouse_pos)) and nail_count == 4:
            if mouse_click == (False, False, False):
                hit_sound()
                nh4_rect.midbottom = mouse_pos
                screen.blit(nh4_surf,nh4_rect)
                n = 0
                nail_count += 1
        elif jc_rect.collidepoint((mouse_pos)) and nail_count == 5:
            if mouse_click == (False, False, False):
                hit_sound()
                nh5_rect.midbottom = mouse_pos
                screen.blit(nh5_surf,nh5_rect)
                n = 0
                nail_count += 1
    
    if mouse_click == (False, False, False):
            n = 0
    
    if nail_count == 6:
        screen.blit(reset_surf,reset_rect)
        if reset_rect.collidepoint((mouse_pos)) and mouse_click == (True, False, False):
            nh1_rect.bottomright = (0,0)
            nh2_rect.bottomright = (0,0)
            nh3_rect.bottomright = (0,0)
            nh4_rect.bottomright = (0,0)
            nh5_rect.bottomright = (0,0)
            nail_count = 1


    pygame.display.update()
    clock.tick(60)