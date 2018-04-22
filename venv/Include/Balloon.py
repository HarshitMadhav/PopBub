import pygame
from random import randint, uniform
from pygame.sprite import  Sprite

class Balloon(Sprite):
    def __init__(self,screen, settings):
        Sprite.__init__(self)
        self.screen=screen
        self.image=pygame.image.load('resources/bub.png')
        self.image_w,self.image_h=self.image.get_size()
        self.speed= uniform(0.75,1.25) * settings.balloon_speed
        #self.speed=0.1

        self.x_position=randint(self.image_w/2,self.screen.get_width()-self.image_w/2)
        max_offset = min(settings.batch_size * self.image_h, self.screen.get_height())
        print (max_offset)
        self.y_position=self.screen.get_height()+self.image_h/2 + randint(0, self.screen.get_height())

        self.update_rect()

    def update(self,time_passed):
        self.y_position -= self.speed * time_passed
        self.update_rect()

    def blitme(self):
        draw_pos=self.image.get_rect().move(self.x_position-self.image_w/2,self.y_position-self.image_h/2)

        self.screen.blit(self.image,draw_pos)

    def update_rect(self):
        self.rect=pygame.Rect(self.x_position-self.image_w/2,self.y_position-self.image_h/2,
                                self.image_w, self.image_h)