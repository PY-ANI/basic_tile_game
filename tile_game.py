import pygame
import random

pygame.init()
win = pygame.display.set_mode((480, 600))
pygame.display.set_caption("TILE GAME")


def draw_blocks():
    global speed, score, life, color, count, blocks, pause
    if count == 0 and pause == False:
        color = random.randrange(4)
        blocks[(120, -40), (180, -40), (240, -40), (300, -40)] = color
        count = 40
    elif pause == False:
        count -= speed

    for pos, colr in blocks.copy().items():
        for indx, i in enumerate(pos):
            if indx == colr:
                pygame.draw.rect(win, (0, 0, 0), (i[0], i[1], width, height))
            else:
                pygame.draw.rect(win, (200, 200, 200),
                                 (i[0], i[1], width, height))
        if pause == False:
            blocks[(pos[0][0], pos[0][1]+speed), (pos[1][0], pos[1][1]+speed), (pos[2][0], pos[2][1]+speed), (pos[3][0], pos[3][1]+speed)] = colr
            del blocks[pos]
        if pos[0][1] > 600 and pause == False:
            del blocks[(pos[0][0], pos[0][1]+1), (pos[1][0], pos[1][1]+1), (pos[2][0], pos[2][1]+1), (pos[3][0], pos[3][1]+1)]
            life -= 1

def display_score():
    global score, life

    score_font= pygame.font.SysFont("consolas", 25)
    score_surf1= score_font.render("Score: ", True, (0, 0, 0))
    score_surf= score_font.render(f"  {score}", True, (0, 0, 0))
    life_surf= score_font.render("Life: ", True, (0, 0, 0))
    life_surf1= score_font.render(f"  {life}", True, (0, 0, 0))
    win.blits([[score_surf1, (4, 0)], [score_surf, (4, 25)], [
              life_surf, (400, 0)], [life_surf1, (400, 25)]])
    if pause == True:
        pause_font= pygame.font.SysFont("comicon", 30)
        pause_surf= pause_font.render("PAUSE", True, (255, 0, 0))
        pause_surf1= score_font.render(
            f"  {pause_count//60}", True, (255, 0, 0))
        win.blits([[pause_surf, (200, 240)], [pause_surf1, (200, 270)]])


def reset():
    global blocks, life, score, count, color, pause

    blocks.clear()
    life= 5
    count= 0
    score= 0
    color= None
    pause= True


def click(mouse):
    global blocks, score, speed

    if mouse[1] < 560 and mouse[1] > 440:
        for pos,i in blocks.copy().items():
            for j,cord in enumerate(pos):
                if (mouse[0]-mouse[0]%60 == cord[0]) and (mouse[1]-mouse[1]%40 == cord[1]-cord[1]%40):
                    score+=1

            if (i == 3):
                break


clock= pygame.time.Clock()
fps= 60
height= 40
width= 60
speed= 1
color= None
score= 0
life= 5
run= True
pause= False
count= 0
pause_count= 0
blocks= {}

while run:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run= False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click(pygame.mouse.get_pos())

    keys= pygame.key.get_pressed()

    if keys[pygame.K_RETURN] and pause == False and pause_count == 0:
        pause= True
        pause_count= 300
    elif pause_count == 0 and pause == True:
        pause= False

    if life < -10:
        reset()

    if pause_count > 0:
        pause_count -= 1

    win.fill((255, 255, 255))

    draw_blocks()
    for i in range(2, 7):
        pygame.draw.line(win, (0, 0, 0), (width*i, 0), (width*i, 600))
    pygame.draw.line(win, (0, 0, 0), (width*2, 0), (width*6, 0))
    pygame.draw.line(win, (0, 255, 0), (width*2, 440), (width*6, 440), 3)
    pygame.draw.line(win, (255, 0, 0), (width*2, 560), (width*6, 560), 3)
    display_score()
    pygame.display.update()

pygame.quit()
Quit()
