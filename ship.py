#Ship For Game
import pygame
import game_functions as gf
from pygame.sprite import Group
class Ship(object):
    def __init__(self,a_setting,screen,aliens):
        self.aliens=aliens

        #set ship image as center as of pygame screen
        self.screen=screen
        self.a_setting=a_setting
        self.image=pygame.image.load('image/shipo.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery
        self.rect.bottom=self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.moving_bullet=False
        
    def blitme(self):#draw ship image to screen
        self.screen.blit(self.image,self.rect)
    def update(self,a_setting,screen,ship,aliens,bullets):
        if self.moving_right:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center +=self.a_setting.ship_speed_factor
        if self.moving_left:
            if self.moving_left and self.rect.left > 0:
                self.center -=self.a_setting.ship_speed_factor
        if self.moving_up:
            if self.moving_up and self.rect.top>0:
                self.rect.centery-=self.a_setting.ship_speed_factor
                
        if self.moving_down:
            if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
                self.rect.centery+=self.a_setting.ship_speed_factor
        if self.moving_bullet:
            
            #gf.fire_bullet(a_setting,screen,ship,bullets)
            #gf.bull(bullets)
            #gf.update_bullets(bullets)
            gf.fire_bullet(a_setting,screen,ship,bullets)
            gf.update_screen(a_setting,screen,ship,aliens,bullets)
            
            
            
        self.rect.centerx = self.center
        #self.rect.y=self.y


