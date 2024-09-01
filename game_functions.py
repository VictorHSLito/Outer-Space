import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):  # Função responsável pela ações de pressionamento de teclas
    if event.key == pygame.K_RIGHT:  # Define o atributo "moving_right" da espaçonave como True
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # Define o atributo "moving_left" da espaçonave como True
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # Aciona o método fire_bullets presente em game_functions
        fire_bullets(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_UP:  # Define o atributo "moving_up" da espaçonave como True
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:  # Define o atributo "moving_down" da espaçonave como True
        ship.moving_down = True
    elif event.key == pygame.K_ESCAPE:  # Encerra o jogo ao pressionar ESC
        sys.exit()


def check_keyup_events(event, ship):  # Função responsável pela ações de "soltura" de teclas
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):  # Função responsável pela detecção de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):  # Função responsável pela atualizações de tela no jogo
    screen.fill(ai_settings.background_colour)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):  # Função responsável pela atualizações de projéteis no jogo
    bullets.update()
    for bullet in bullets.copy():  # Verifica se os projéteis saíram da tela
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  # Caso sim, o laço "for" irá apagá-las para que não consuma muita memória


def fire_bullets(ai_settings, screen, ship, bullets):   # Função que limitará os projéteis disparados pela espaçonave
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_alien_x): #Loop que criará a frota de alienigenas
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width  # Limita até onde os alienigenas podem chegar na borda horizontal
    number_alien_x = int(available_space_x / 2 * alien_width)  # Calcula quantos alienigenas cabem na tela
    return number_alien_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number  # Define o espaço entre os alienigenas, no caso o espaço é de 2 alienigenas
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
        """"Determina o número de linhas de alienigenas que cabem na tela"""
        available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
        number_rows = int(available_space_y/(2*alien_height))
        return number_rows