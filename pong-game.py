import pygame
import math
import random

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("pong")
clock = pygame.time.Clock()

#Define paddles (from left to right)
l_paddle = pygame.Rect(50, 250, 20, 100)
r_paddle = pygame.Rect(730, 250, 20, 100)
paddle_speed = 5

#Define ball
ball = pygame.Rect(390, 290, 20, 20)
ball_speed = [0, 0]
base_speed = 5

#score
score = [0, 0]
font = pygame.font.Font(None, 36)

#Function to reset the ball
def reset_ball():
    ball.center = (400, 300)
    angle = random.uniform(-math.pi/4, math.pi/4)
    direct = random.choice((-1, 1))
    ball_speed[0] = direct * base_speed * math.cos(angle)
    ball_speed[1] = base_speed * math.sin(angle)
    
#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Player controls
    keys = pygame.key.get_pressed()
    
    #Left paddle (player 1: W and S)
    if keys[pygame.K_w] and l_paddle.top > 0:
        l_paddle.y -= paddle_speed
    if keys[pygame.K_s] and l_paddle.bottom < 600:
        l_paddle.y += paddle_speed
        
    #Right paddle (player 2: Arrows keys)
    if keys[pygame.K_UP] and r_paddle.top > 0:
        r_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and r_paddle.bottom < 600:
        r_paddle.y += paddle_speed
        
    #start the ball if stationary
    if ball_speed ==[0, 0]:
        reset_ball()
        
    #move ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    
    #bounce off top and bottom walls
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed[1] = -ball_speed[1]
        
    #bounce off paddle and increase speed
    if ball.colliderect(l_paddle) or \
        ball.colliderect(r_paddle):
            ball_speed[0] = -ball_speed[0] * 1.1
            ball_speed[1] *= 1.1
            
    #score points and reset ball
    if ball.left <= 0:
        score[1] += 1
        reset_ball()
    if ball.right >= 800:
        score[0] += 1
        reset_ball()
        
    #draw everything 
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), l_paddle)
    pygame.draw.rect(screen, (0, 255, 0), r_paddle)
    pygame.draw.ellipse(screen, (255, 0, 0), ball)
    score_text = font.render(f"{score[0]} - {score[1]}",
                            True,(255, 255, 255))
    screen.blit(score_text, (380, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()