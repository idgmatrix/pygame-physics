import pygame, sys, math

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Projectile Motion')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

delta_t = 0.01
m = 1
g = 9.8
k = 0.2

x = 0
y = 300

angle = 45
theta = math.radians(angle)

v = 100
vx = v * math.cos(theta)
vy = -v * math.sin(theta)

while True:
    screen.fill(BLACK)

    fx = -k*vx
    fy = m*g - k*vy

    vx = vx + (fx / m) * delta_t
    vy = vy + (fy / m) * delta_t

    x = x + vx * delta_t
    y = y + vy * delta_t

    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)


