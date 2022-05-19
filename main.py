import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jesus Game')
clock = pygame.time.Clock()

font = pygame.font.Font('./font/font.ttf', 45)
sm_font = pygame.font.Font('./font/font.ttf', 20)

background = pygame.Surface((800,600))
background.fill('DarkGrey')

c_surf = pygame.image.load('./graphics/Cross.png').convert_alpha()
c_rect = c_surf.get_rect(center = (400,300))

j_surf = pygame.image.load('./graphics/Jesus.png').convert_alpha()
j_rect = j_surf.get_rect(bottomright = (0,0))

b_surf = pygame.image.load('./graphics/Bucket.png').convert_alpha()
b_rect = b_surf.get_rect(bottomleft = (5,595))

rotated_j_surf = pygame.transform.rotate(j_surf, 90).convert_alpha()
rotated_j_rect = rotated_j_surf.get_rect(midleft = (0,560))
x = 0

jc_surf = pygame.image.load('./graphics/JesusOnCross.png').convert_alpha()
jc_rect = jc_surf.get_rect(center = (400,300))

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
        screen.blit(jc_surf,jc_rect)
        screen.blit(b_surf,b_rect)
        screen.blit(text_nail_surf,text_nail_rect)
        screen.blit(text_label_surf,text_label_rect)


    pygame.display.update()
    clock.tick(60)