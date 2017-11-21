import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Fractal: Mandelbrot Set")

iteration = 50

for i in range(0, 640):
    for j in range(0,480):
        cx = i / 640.0 * 4.0 - 2.5
        cy = j / 480.0 * 3.0 - 1.5
        c = cx + cy*1j
        z = 0.0 + 0.0*1j

        color = (0,0,0)
        for ii in range(iteration):
            z = z**2 + c
            if (abs(z) > 2.0):
                col = ii / iteration * 255.0
                color = (0,col,col)
                break

        screen.set_at((i, j), color)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
