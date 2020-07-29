#Game
#import sys #no Longer needed because it is used in game_function
import pygame
from setting import Setting
from ship import Ship
#from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from ggame_stats import GameStats

def run_game():
    pygame.init()
    """This is setting function defined earlier whose instance is used here"""
    a_setting=Setting()
    
    screen=pygame.display.set_mode((a_setting.screen_width,a_setting.screen_height))
    #alien=Alien(a_setting,screen)
    pygame.display.set_caption("Alien")
    stats=GameStats(a_setting)
    #bg_co=(255,0,0) #no longer needed because it is used in setting
    
    bullets=Group()
    aliens=Group()
    ship=Ship(a_setting,screen,aliens)
    gf.create_fleet(a_setting,screen,ship,aliens)
    while True:
        
        gf.check_events(a_setting,screen,ship,bullets)
        ship.update(a_setting,screen,ship,aliens,bullets)
        gf.update_bullets(a_setting,screen,ship,aliens,bullets)
        #gf.update_bullets(bullets)
        gf.update_aliens(a_setting,stats,screen,ship,aliens,bullets)
        
        gf.update_screen(a_setting,screen,ship,aliens,bullets)
        
run_game()

