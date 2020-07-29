#bullet for your game
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,a_setting,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,a_setting.bullet_width,a_setting.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y= float(self.rect.y)
        self.color=a_setting.bullet_color
        self.speed_factor=a_setting.bullet_speed_factor
        
    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        