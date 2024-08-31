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


def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2*alien_width  # Limita até onde os alienigenas podem chegar na borda horizontal
    number_alien_x = int(available_space_x/2*alien_width)  # Calcula quantos alienigenas cabem na tela

    for alien_number in range(number_alien_x):  #Loop que criará a frota de alienigenas
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2*alien_width*alien_number  # Define o espaço entre os alienigenas, no caso o espaço é de 2 alienigenas
        alien.rect.x = alien.x
        aliens.add(alien)