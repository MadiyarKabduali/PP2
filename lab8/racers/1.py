import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
SCORE = 0
WHITE = (255, 255, 255)

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coin Racer")

# Load images
image_background = pygame.image.load("AnimatedStreet.png")
image_player = pygame.image.load("Player.png")
image_enemy = pygame.image.load("Enemy.png")
image_coin = pygame.image.load("Coin.png")

# Load sounds
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)
sound_crash = pygame.mixer.Sound("crash.wav")
sound_coin = pygame.mixer.Sound("coin_hit.mp3")

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep player within bounds
        self.rect.clamp_ip(screen.get_rect())


# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 7
        self.generate_random_position()

    def generate_random_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.generate_random_position()


# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(image_coin, (30, 30))
        self.rect = self.image.get_rect()
        self.generate_random_position()

    def generate_random_position(self):
        self.rect.x = random.randint(50, SCREEN_WIDTH - 50)
        self.rect.y = random.randint(100, SCREEN_HEIGHT - 200)

    def update(self):
        pass  # Coin does not move on its own


# Create sprites
player = Player()
enemy = Enemy()
coin = Coin()

# Sprite groups
all_sprites = pygame.sprite.Group(player, enemy, coin)
enemy_sprites = pygame.sprite.Group(enemy)
coin_sprites = pygame.sprite.Group(coin)

# Clock
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Coin collection
    if pygame.sprite.spritecollideany(player, coin_sprites):
        sound_coin.play()
        SCORE += 1
        coin.generate_random_position()

    # Collision with enemy
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        running = False
        break

    # Draw
    screen.blit(image_background, (0, 0))
    all_sprites.draw(screen)
    coin_text = font_small.render(f"Coins: {SCORE}", True, "black")
    screen.blit(coin_text, (SCREEN_WIDTH - coin_text.get_width() - 10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
