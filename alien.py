import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('Images/alien.png')  # Carrega a imagem do alienígena e define seu atributo rect
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width  # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)  # Armazena a posição do alienígena

    def blitme(self):  # Desenha o alienígena na sua posição atual
        self.screen.blit(self.image, self.rect)
