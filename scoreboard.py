import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """Classe responsável pela pontuação do jogo"""

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Transforma a pontuação em imagem"""
        rounded_score = round(self.stats.score, -1)  # Arredonda a pontuação para um múltiplo de 10 mais próximo
        score_str = "{:,}".format(rounded_score)  # Mostra a pontuação formata
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.background_colour)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Transforma a pontuação máxima em imagem"""
        high_score = round(self.stats.score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_img = self.font.render(high_score_str, True, self.text_color,
                                               self.ai_settings.background_colour)
        # Centraliza a pontuação máxima na parte superior da tela
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Transforma o nível em imagem"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,
                                            self.ai_settings.background_colour)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Mostram quantas 'vidas' ainda restam"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            """Loop responsável por criar uma aeronave ao lado da outra"""
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Desenha as pontuaçãoes na tela"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
