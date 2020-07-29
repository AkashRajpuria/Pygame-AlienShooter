import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,a_setting,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.a_setting=a_setting
        self.image=pygame.image.load('image/alien2.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.x=self.screen_rect.top+1
        self.rect.y=self.screen_rect.left+1
        self.x=float(self.rect.x)
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        self.fleet_direction=1
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self,a_setting):
        
        self.x+=a_setting.alien_speed_factor*a_setting.fleet_direction
        self.rect.x=self.x

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
        

