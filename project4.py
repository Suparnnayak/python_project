#importing pygame and displaying screen requirements
import pygame  
import random
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Copter Game")

#displaying constants and colors

FPS=60
GRAVITY=0.5
FLAP_STRENGTH=-10
OBSTACLE_GAP=200
OBSTACLE_WIDTH=70
OBSTACLE_SPEED=5
UPWARD_SPEED=-5
DOWNWARD_SPEED=5

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
SKY_BLUE=(135,206,235)
GREY=(169,169,169)

#VARIABLES

helicopter_rect=pygame.Rect(100,HEIGHT//2,42,28)
velocity=0
obstacles=[]
score=0
game_over=False
#fonts
font=pygame.font.Font(None,36)

def create_obstacle():
    y=random.randint(100,HEIGHT-100-OBSTACLE_GAP)
    top_rect=pygame.Rect(WIDTH,0,OBSTACLE_WIDTH,y)
    bottom_rect=pygame.Rect(WIDTH,y+OBSTACLE_GAP,OBSTACLE_WIDTH,HEIGHT-(y+OBSTACLE_GAP))
    return top_rect,bottom_rect

def draw_helicopter(rect):
    pygame.draw.ellipse(screen,RED,rect)

    cockpit_rect=pygame.Rect(rect.x+14,rect.y+7,12,7)
    pygame.draw.ellipse(screen,BLUE,cockpit_rect)

    top_rotor_rect=pygame.Rect(rect.x-33,rect.y-8,rect.width+66,6)
    pygame.draw.ellipse(screen,SKY_BLUE,top_rotor_rect)
    rotor_block_rect=pygame.Rect(rect.x+rect.width//2-2,rect.y,4,4)
    pygame.draw.rect(screen,BLACK,rotor_block_rect)

    pygame.draw.rect(screen,GREY,(rect.x-28,rect.y+rect.height//4-4,28,7))

    pygame.draw.rect(screen,SKY_BLUE,(rect.x-35,rect.y+rect.height//4-4,7,14))

    pygame.draw.rect(screen,BLACK,(rect.x+7,rect.y+rect.height-3,rect.width-14,3))
    pygame.draw.rect(screen,BLACK,(rect.x+3,rect.y+rect.height,3,6))
    pygame.draw.rect(screen,BLACK,(rect.x+rect.width-7,rect.y+rect.height,3,6))

    

clock=pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.QUIT()
            exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        velocity=UPWARD_SPEED
    elif keys[pygame.K_DOWN]:
        velocity=DOWNWARD_SPEED
    else:
        velocity+=GRAVITY


    if not game_over:
        helicopter_rect.y+=velocity

        if helicopter_rect.top < 0 or helicopter_rect.bottom > HEIGHT:
            game_over=True

        for obstacle in obstacles:
            obstacle[0].x -= OBSTACLE_SPEED
            obstacle[1].x -= OBSTACLE_SPEED
        if len(obstacles) == 0 or obstacles[-1][0].x < WIDTH -300:
            obstacles.append(create_obstacle())
        if obstacles[0][0].x <- OBSTACLE_WIDTH:
            obstacles.pop(0)
            score +=1

        for top_rect,bottom_rect in obstacles:
            if helicopter_rect.colliderect(top_rect) or helicopter_rect.colliderect(bottom_rect):
                game_over=True

    screen.fill(WHITE)
    draw_helicopter(helicopter_rect)

    for top_rect,bottom_rect in obstacles:
        pygame.draw.rect(screen,GREEN,top_rect)
        pygame.draw.rect(screen,GREEN,bottom_rect)

    score_text=font.render(f"score:{score}",True,BLACK)
    screen.blit(score_text,(10,10))

    if game_over:
        game_over_text=font.render("Game over ...!!! Press R to Restart! Fly with Arrow keys (up/down)",True,BLACK)
        screen.blit(game_over_text,(WIDTH//2-game_over_text.get_width()//2,HEIGHT//2))
    pygame.display.flip()

    if game_over and keys[pygame.K_r]:
        helicopter_rect.y=HEIGHT//2
        velocity=0
        obstacles.clear()
        score=0
        game_over=False