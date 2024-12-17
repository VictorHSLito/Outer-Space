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

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Verifica se o alienígena atingiu a borda da tela"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
