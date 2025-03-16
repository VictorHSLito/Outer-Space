import pygame.display


class Settings:  # Classe das principais configurações do jogo
    def __init__(self):
        self.screen_width = 1280  # Atributo que define a largura da tela
        self.screen_height = 720  # Atributo que define a altura da tela
        self.info = pygame.display.Info()
        self.monitor_screen_widht = self.get_dimensions_of_width()
        self.monitor_screen_height = self.get_dimensions_of_height()
        self.game_on_full_screen = False
        self.background_colour = (230, 230, 230)  # Atributo que define a cor de fundo do jogo
        self.ship_limit = 3

        self.bullet_width = 3  # Atributo que define a largura dos projéteis
        self.bullet_height = 15  # Atributo que define o tamanho dos projéteis
        self.bullet_colour = (60, 60, 60)  # Atributo que define a cor dos projéteis
        self.bullets_allowed = 5  # Atributo que define a quantidade máxima de projéteis na tela

        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5  # Atributo que define a velocidade da espaçonave
        self.alien_speed_factor = 1  # Atributo que define a velocidade de movimento dos alienígenas
        self.bullet_speed_factor = 1.75  # Atributo que define a velocidade dos projéteis
        self.fleet_direction = 1  # 1 representa para direita e -1 para a esquerda

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def get_dimensions_of_width(self):
        self.monitor_screen_widht = self.info.current_w
        return self.monitor_screen_widht

    def get_dimensions_of_height(self):
        self.monitor_screen_height = self.info.current_h
        return self.monitor_screen_height
