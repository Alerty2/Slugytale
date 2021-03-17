import pygame
#import  main
global vida
vida = 20
global daño
daño = 0
###########CLASE PADRE ENEMIGOS#############
class Enemigo(pygame.sprite.Sprite):
    def __init__(self,imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
   #@# MOMIA #@#
class momia(Enemigo):
    def __init__(self,imagen):
        super().__init__(imagen)
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
