import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("WOLF GAME!")

# Background
background = pygame.image.load("C:/Users/ariro/Downloads/aplah wolf sigma.jpg")
background = pygame.transform.scale(background, (800, 600))  # Resize the background to fit the screen

# Clock for frame rate
clock = pygame.time.Clock()

# Player class
class Player(object):
    def __init__(self):
        self.img = pygame.image.load("C:/Users/ariro/Downloads/sigma wolf.WEBP")
        self.img = pygame.transform.scale(self.img, (200, 200))  # Resize to 50x50 pixels
        self.x = 370
        self.y = 480
        self.x_change = 0
        self.y_change = 0

# Enemy class
class Enemy(object):
    def __init__(self, x, y):
        self.img = pygame.image.load("C:/Users/ariro/Downloads/EVIL WOLF.png")
        self.img = pygame.transform.scale(self.img, (70, 70))  # Resize to 50x50 pixels
        self.x = x
        self.y = y
        self.x_change = random.choice([-3, 3])  # Random horizontal speed (left or right)

# Bullet class
class Bullet(object):
    def __init__(self, x, y):
        self.img = pygame.image.load("C:/Users/ariro/Downloads/sopa2.webp")
        self.img = pygame.transform.scale(self.img, (20, 20))  # Resize to 20x20 pixels
        self.x = x
        self.y = y
        self.y_change = -5  # Bullet moves upward

# Draw functions
def draw_player(img, x, y):
    screen.blit(img, (x, y))

def draw_enemy(img, x, y):
    screen.blit(img, (x, y))

def draw_bullet(img, x, y):
    screen.blit(img, (x, y))

# Collision detection
def is_collision(enemy, bullet):
    distance = ((enemy.x - bullet.x) ** 2 + (enemy.y - bullet.y) ** 2) ** 0.5
    return distance < 30  # Collision threshold

# Create player
player = Player()

# Create enemies
enemies = []
for _ in range(5):  # Create 5 enemies
    x = random.randint(0, 750)
    y = random.randint(50, 150)
    enemies.append(Enemy(x, y))

# Bullets list
bullets = []

# Score
score = 0
font = pygame.font.Font(None, 36)

def main_loop():
    global score
    running = True
    while running:
        # Fill the screen and draw the background
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Check for key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  # Move left
                    player.x_change = -5
                if event.key == pygame.K_d:  # Move right
                    player.x_change = 5
                if event.key == pygame.K_w:  # Move up
                    player.y_change = -5
                if event.key == pygame.K_s:  # Move down
                    player.y_change = 5
            # Check for key releases
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_a, pygame.K_d]:
                    player.x_change = 0
                if event.key in [pygame.K_w, pygame.K_s]:
                    player.y_change = 0
            # Check for mouse click to shoot
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    bullets.append(Bullet(player.x + 15, player.y))  # Center bullet on player

        # Update player position
        player.x += player.x_change
        player.y += player.y_change

        # Ensure the player stays within screen bounds
        player.x = max(0, min(player.x, 800 - player.img.get_width()))
        player.y = max(0, min(player.y, 600 - player.img.get_height()))

        # Update enemies
        for enemy in enemies:
            enemy.x += enemy.x_change
            # Reverse direction if the enemy hits the screen bounds
            if enemy.x <= 0 or enemy.x >= 750:
                enemy.x_change *= -1

        # Update bullets
        for bullet in bullets[:]:
            bullet.y += bullet.y_change
            if bullet.y < 0:  # Remove bullet if it moves off-screen
                bullets.remove(bullet)

        # Check for collisions
        for enemy in enemies:
            for bullet in bullets[:]:
                if is_collision(enemy, bullet):
                    # Reset the enemy's position instead of removing it
                    enemy.x = random.randint(0, 750)
                    enemy.y = random.randint(50, 150)
                    bullets.remove(bullet)
                    score += 1
                    break

        # Draw the player
        draw_player(player.img, player.x, player.y)

        # Draw the enemies
        for enemy in enemies:
            draw_enemy(enemy.img, enemy.x, enemy.y)

        # Draw the bullets
        for bullet in bullets:
            draw_bullet(bullet.img, bullet.x, bullet.y)

        # Draw the score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Limit the frame rate to 60 FPS

main_loop()
pygame.quit()