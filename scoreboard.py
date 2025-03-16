import pygame.font


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

    def show_score(self):
        """Desenha as pontuaçãoes na tela"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)