import pygame
import math
import time

pygame.init()

window_size = (1200, 800)

screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("My Pygame Watch")

display = (255, 255, 255)
clock_color = (0, 0, 0)
minute_hand_color = (0, 0, 0)
second_hand_color = (255, 0, 0)

clock_position = (600, 400)
clock_radius = 150
minute_hand_length = 150
minute_hand_width = 5
second_hand_length = 170
second_hand_width = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(display)
    screen.blit(pygame.image.load('clock.jpeg'), (365, 165))

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = math.radians(minutes * 6)
    second_angle = math.radians(seconds * 6)

    
    minute_hand_x = clock_position[0] + minute_hand_length * math.cos(minute_angle - math.pi / 2)
    minute_hand_y = clock_position[1] + minute_hand_length * math.sin(minute_angle - math.pi / 2)
    pygame.draw.line(screen, minute_hand_color, clock_position, (minute_hand_x, minute_hand_y), minute_hand_width)

    
    second_hand_x = clock_position[0] + second_hand_length * math.cos(second_angle - math.pi / 2)
    second_hand_y = clock_position[1] + second_hand_length * math.sin(second_angle - math.pi / 2)
    pygame.draw.line(screen, second_hand_color, clock_position, (second_hand_x, second_hand_y), second_hand_width)

    pygame.display.flip()

    time.sleep(1)

pygame.quit()
