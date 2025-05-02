import pygame
import random
pygame.init()
pygame.mixer.init() 

def background():
    global bg_x 
    SCREEN.blit(bg, (bg_x, 0))
    SCREEN.blit(bg, (bg_x + 1200, 0))
    bg_x -= bg_speed
    if bg_x <= -1200:
        bg_x = 0
        
def set_score():
    player_score = font.render(f"PLAYER SCORE: {player_num}",True, (colour))
    enemy_score = font.render(f"ENEMY SCORE: {enemy_num}",True, (colour))
    SCREEN.blit(player_score, (60, 20))
    SCREEN.blit(enemy_score, (900, 20))

def movement():
    key = pygame.key.get_pressed()
    if key[pygame.K_s]== True:  
        player.y += 15
    elif key[pygame.K_w]== True:
        player.y -= 15
    if key[pygame.K_UP]== True:  
        enemy.y -= 15
    elif key[pygame.K_DOWN]== True:
        enemy.y += 15
        
def bullet_hit():
    global bullet_speed_x, bullet_speed_y
    bullet.x += bullet_speed_x
    bullet.y += bullet_speed_y
    
    if bullet.colliderect(player):
        hit_sound.play()
        if bullet_speed_x > 0:
            bullet_speed_x += 2
        elif bullet_speed_x < 0:
            bullet_speed_x -= 2
        bullet_speed_x *= -1
    elif bullet.colliderect(enemy):
        hit_sound.play()
        if bullet_speed_x > 0:
            bullet_speed_x += 2
        elif bullet_speed_x < 0:
            bullet_speed_x -= 2
        bullet_speed_x *= -1
    elif bullet.top <= 0 or bullet.bottom >= SCREEN.get_height():
        bullet_speed_y *= -1
    
        
def bullet_score():
    global bullet_speed_x, player_num, enemy_num
    if bullet.right >= SCREEN.get_width():
        score_sound.play()
        bullet_speed_x *= -1
        player_num += 1
        bullet.x = SCREEN.get_width() // 2
        bullet.y = SCREEN.get_height() // 2
        bullet_speed_x = 9
    elif bullet.left <= 0 :
        score_sound.play()
        bullet_speed_x *= -1
        enemy_num += 1
        bullet.x = SCREEN.get_width() // 2
        bullet.y = SCREEN.get_height() // 2
        bullet_speed_x = 9
        
def enemy_movement():
    randomness = random.randint(-20, 20)
    if enemy.centery > bullet.centery + randomness:
        enemy.y -= random.randint(6, 9)
    elif enemy.centery < bullet.centery - randomness:
        enemy.y += random.randint(6, 9)
    
SCREEN = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

bg = pygame.image.load("C:/Users/ariro/Downloads/sky.jpg")
bg = pygame.transform.scale(bg, (1200, 700))
bg_speed = 1.5
bg_x = 0

font = pygame.font.Font("C:/Users/ariro/Downloads/Teko,Ubuntu/Teko/static/Teko-Light.ttf", 50) 
colour = (44, 48, 56)

hit_sound = pygame.mixer.Sound("C:/Users/ariro/Downloads/hit-soundvideo-game-type-230510.mp3")
score_sound = pygame.mixer.Sound("C:/Users/ariro/Downloads/point.mp3")

player_image = pygame.image.load("Python codes/Pong/arts/Player.png") 
player_image = pygame.transform.scale(player_image, (35, 250))
player = player_image.get_rect()
player.left = 0+14
player_num = 0

enemy_image = pygame.image.load("Python codes/Pong/arts/Enemy.png") 
enemy_image = pygame.transform.scale(enemy_image, (35, 250))
enemy = enemy_image.get_rect()
enemy.right = 1200-14
enemy_num = 0

bullet_motion = pygame.image.load("Python codes/Pong/arts/BallMotion.png")
bullet_image = pygame.image.load("Python codes/Pong/arts/Ball.png") 
bullet_image = pygame.transform.scale(bullet_image, (35, 35))
bullet = bullet_image.get_rect()
bullet_speed_x = 9
bullet_speed_y = 10

def main():
    run = True
    while run:
        background()
        
        set_score()
        
        SCREEN.blit(bullet_image, bullet)
        SCREEN.blit(enemy_image, enemy)
        SCREEN.blit(player_image, player)
        
        movement()
        
        bullet_hit()
        
        bullet_score()
        
        enemy_movement()
        
        SCREEN_RECT = SCREEN.get_rect()
        player.clamp_ip(SCREEN_RECT)
        enemy.clamp_ip(SCREEN_RECT)
        bullet.clamp_ip(SCREEN_RECT)
        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    
if __name__ == "__main__":
    main()