import pygame
import random
import time
pygame.init()


dis_width = 800
dis_height = 800

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption('Best Snake ever from Sacha')
game_over=False

x1 = 20
y1 = 20

x1_update = 0
y1_update = 0

snake_List = []
length_of_snake = 1

foodx = round(random.randrange(0, dis_width - 20) / 20.0) * 20.0
foody = round(random.randrange(0, dis_width - 20) / 20.0) * 20.0

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

clock = pygame.time.Clock()


font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, (0,0,255), [x[0], x[1], 20, 20])
    

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, (125,125,125))
    dis.blit(value, [0, 0])
    return score

while not game_over:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_update = -20
                y1_update = 0
            elif event.key == pygame.K_RIGHT:
                x1_update = 20
                y1_update = 0
            elif event.key == pygame.K_UP:
                y1_update = -20
                x1_update = 0
            elif event.key == pygame.K_DOWN:
                y1_update = 20
                x1_update = 0

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True


    x1 += x1_update
    y1 += y1_update
    dis.fill(white)

    pygame.draw.rect(dis, (random.randrange(0,255,1),random.randrange(0,255,1),random.randrange(0,255,1)), [foodx, foody, 20, 20])
    pygame.draw.rect(dis,(0,0,255),[x1,y1,20,20])

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)

    if len(snake_List) > length_of_snake:
        del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                message("Perdu :)",red)
                time.sleep(2)
                pygame.quit()
                quit()
 
        our_snake(snake_List)
        speed = your_score(length_of_snake - 1)
        if speed / 3 == 0:
            upgrade = upgrade + 2



    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, dis_width - 20) / 20.0) * 20.0
        foody = round(random.randrange(0, dis_height - 20) / 20.0) * 20.0
        length_of_snake += 1

    upgrade = clock.tick(15)

message("You lost",red)
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()