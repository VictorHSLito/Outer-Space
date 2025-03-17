import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('Images/Aeronave.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)  # Define o centro x da espaçonave
        self.centery = float(self.rect.centery)  # Define o centro y da espaçonave
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:  # Limita a espaçonave de ultrapassar a lateral direita
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:  # Limita a espaçonave de ultrapassar a lateral esquerda
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:  # Limita a espaçonave de ultrapassar a borda superior
            self.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:  # Limita a espaçonave de ultrapassar a borda inferior
            self.centery += 1

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):  # Desenha a espaçonave na sua posição atual
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - (self.rect.height / 2)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
