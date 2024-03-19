class Settings:  # Classe das principais configurações do jogo
    def __init__(self):
        self.screen_width = 1280  # Atributo que define a largura da tela
        self.screen_height = 720 # Atributo que define a altura da tela
        self.background_colour = (230, 230, 230)  # Atributo que define a cor de fundo do jogo
        self.ship_speed_factor = 1.5  # Atributo que define a velocidade da espaçonave

        self.bullet_speed_factor = 1  # Atributo que define a velocidade dos projéteis
        self.bullet_width = 3  # Atributo que define a largura dos projéteis
        self.bullet_height = 15  # Atributo que define o tamanho dos projéteis
        self.bullet_colour = (60, 60, 60)  # Atributo que define a cor dos projéteis
        self.bullets_allowed = 5  # Atributo que define a quantidade máxima de projéteis na tela