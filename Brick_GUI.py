#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Brick_GUI(pygame.sprite.Sprite):

    # Các giá trị của khối gạch
    def __init__(self,brick,unit):
        super(Brick_GUI, self).__init__()
        self.unit = int(unit)

        self.length = brick.length

        if brick.isVetical:
            self.img_load = pygame.image.load('image/vertical.png')
            self.image = pygame.transform.scale(self.img_load,(self.unit,self.length*self.unit))
        else:
            if brick.id == 1:
                self.img_load = pygame.image.load('image/object.png')
            else:
                self.img_load = pygame.image.load('image/horizontal.png')
            self.image = pygame.transform.scale(self.img_load,(self.unit*self.length,self.unit))

        self.rect = self.image.get_rect()
        self.rect.topleft = [(brick.position[1])*self.unit + 12,(brick.position[0]+1)*self.unit + 108]

    def moveVertical(self,moves,pixel):
        tmp = self.rect.topleft[1]
        if moves < 0:
            while self.rect.topleft[1] >= ( tmp + moves*self.unit):
                self.rect.y = self.rect.topleft[1] + moves*pixel
        else:
            while self.rect.topleft[1] <= ( tmp + moves*self.unit):
                #print(self.rect.topleft[1])
                self.rect.y = self.rect.topleft[1] + moves*pixel
                #self.rect.move_ip(0,1)

    def moveHorizontal(self,moves,pixel):
        tmp = self.rect.topleft[0]
        if moves < 0:
            while self.rect.topleft[0] >= (tmp + moves*self.unit):
                #self.rect.x += moves*pixel
                self.rect.x = self.rect.topleft[0] + moves*pixel
        else:
            while self.rect.topleft[0] <= (tmp + moves*self.unit):
                #self.rect.x += moves*pixel
                self.rect.x = self.rect.topleft[0] + moves*pixel