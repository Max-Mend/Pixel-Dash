import pygame
from pygame.locals import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_y = 0
        self.jump_power = -12
        self.gravity = 1
        self.on_ground = False
        self.speed_x = 5

        self.original_img = pygame.image.load('assets/player/block.png').convert_alpha()
        self.img = self.original_img
        self.rect = self.img.get_rect(topleft=(self.x, self.y))

        self.angle = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[K_SPACE] and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

        #self.x += self.speed_x    #move player to left 
        self.vel_y += self.gravity
        self.y += self.vel_y

        if self.y >= 600 - self.rect.height:
            self.y = 600 - self.rect.height
            self.vel_y = 0
            self.on_ground = True
            self.angle = (round(self.angle / 90) * 90) % 360

        self.rect.topleft = (self.x, self.y)

    def update(self):
        self.movement()
        if not self.on_ground:
            self.angle = (self.angle + 10) % 360
            self.img = pygame.transform.rotate(self.original_img, self.angle)
            self.rect = self.img.get_rect(center=self.rect.center)
        else:
            self.img = pygame.transform.rotate(self.original_img, self.angle)
            self.rect = self.img.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.img, self.rect.topleft)
