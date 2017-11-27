#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:25:54 2017

@author: kaswan
"""

import pygame, sys, math

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
WIDTH = 400
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Verlet Particle System')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Particle:
    def __init__(self, x, y, m = 1.0):
        self.m = m
        self.x = x
        self.y = y
        self.oldx = x - 5
        self.oldy = y
        self.newx = x
        self.newy = y
        self.ax = 0
        self.ay = 9.8
        
    def update(self, delta_t):
        # Collision Process
        if self.x < 0 or self.x > WIDTH:
            self.x, self.oldx = self.oldx, self.x
        if self.y < 0 or self.y > HEIGHT:
            self.y, self.oldy = self.oldy, self.y

        # Verlet Integrator
        self.newx = 2.0 * self.x - self.oldx + self.ax * delta_t * delta_t 
        self.newy = 2.0 * self.y - self.oldy + self.ay * delta_t * delta_t 
        self.oldx = self.x
        self.oldy = self.y
        self.x = self.newx
        self.y = self.newy

    def draw(self, surf, size):
        pygame.draw.circle(surf, WHITE, (int(self.x), int(self.y)), size)
        
delta_t = 0.1

# create particles
particles = []
p = Particle(0, 0)
particles.append(p)

while True:
    #screen.fill(BLACK)

    # particle update
    for i in range(len(particles)):
        particles[i].update(delta_t)

    # particle draw
    for i in range(len(particles)):
        particles[i].draw(screen, 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
