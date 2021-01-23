import pygame

# Starting project
pygame.init()

# Making screen
window = pygame.display.set_mode((800, 600))

# Change title
pygame.display.set_caption(" Space Invaders")
icon = pygame.image.load("spaceship.png")

# Change icon
pygame.display.set_icon(icon)

# Adding an image
img = pygame.image.load("space-invaders.png")

playerx = 360
playery = 480
changex = 0


def player(x, y):
    window.blit(img, (x, y))


# Game Loop
running = True

while running:
    # Change color of screen
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changex = -0.3
            if event.key == pygame.K_RIGHT:
                changex = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changex = 0

    if playerx <=0:
        playerx = 0
    if playerx >=736:
        playerx = 736

    playerx += changex
    player(playerx, playery)
    pygame.display.update()