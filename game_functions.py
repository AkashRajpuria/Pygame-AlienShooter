#Game Function
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def check_events(a_setting,screen,ship,bullets):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                check_keydown_events(event,a_setting,screen,ship,bullets)
            elif event.type==pygame.KEYUP:
                check_keyup_events(event,ship)
def check_keydown_events(event,a_setting,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_UP:
        ship.moving_up=True
    elif event.key==pygame.K_DOWN:
        ship.moving_down=True
    elif event.key==pygame.K_SPACE:
        ship.moving_bullet=True
        
        
       
def fire_bullet(a_setting,screen,ship,bullets):
     if len(bullets)<a_setting.bullets_allowed:
        new_bullet=Bullet(a_setting,screen,ship)
        bullets.add(new_bullet)
        
    
        
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right= False
    elif event.key==pygame.K_LEFT:
        ship.moving_left= False
    elif event.key==pygame.K_UP:
        ship.moving_up=False
    elif event.key==pygame.K_DOWN:
        ship.moving_down=False
    elif event.key==pygame.K_SPACE:
        ship.moving_bullet=False
            
                        
def update_screen(a_setting,screen,ship,aliens,bullets):
    
    screen.fill(a_setting.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    pygame.display.flip()
    
def update_bullets(a_setting,screen,ship,aliens,bullets):
    
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens)==0:
        bullets.empty()
        create_fleet(a_setting,screen,ship,aliens)
def get_number_aliens_x(a_setting,alien_width):
    available_space_x=a_setting.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x

def create_alien(a_setting,screen,aliens,alien_number,row_number):
    
    alien=Alien(a_setting,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)
    

def create_fleet(a_setting,screen,ship,aliens):
    alien=Alien(a_setting,screen)
    number_aliens_x=get_number_aliens_x(a_setting,alien.rect.width)
    number_rows=get_number_rows(a_setting,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range (number_aliens_x):
            create_alien(a_setting,screen,aliens,alien_number,row_number)
            

def get_number_rows(a_setting,ship_height,alien_height):
    available_space_y=(a_setting.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows
    

        
def update_aliens(a_setting,stats,screen,ship,aliens,bullets):
    check_fleet_edges(a_setting,aliens)
    aliens.update(a_setting)
    if pygame.sprite.spritecollideany(ship,aliens):
        print("Hogya Beta")

def check_fleet_edges(a_setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            
            change_fleet_direction(a_setting,aliens)
            break

def change_fleet_direction(a_setting,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=a_setting.fleet_drop_speed
    a_setting.fleet_direction*=-1


    
    
