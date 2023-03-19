import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 600))

x = 300
y = 300
color = (255, 0, 0)
radius = 25
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >= 38:
        x -= 20
    if keys[pygame.K_RIGHT] and x <= 1160:
        x += 20
    if keys[pygame.K_UP] and y >= 38:
        y -= 20
    if keys[pygame.K_DOWN] and y <= 570:
        y += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y,), 25)
    pygame.display.update()
pygame.quit()