import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, stats, ship,
                         play_button, aliens,
                         bullets):  # Função responsável pela ações de pressionamento de teclas
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
    elif event.key == pygame.K_p:
        start_game_from_key(ai_settings, screen, stats, ship, aliens, bullets)
    elif event.key == pygame.K_F11:
        enter_or_exit_full_screen_mode(ai_settings)


def check_keyup_events(event, ship):  # Função responsável pela ações de "soltura" de teclas
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens,
                 bullets):  # Função responsável pela detecção de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship,
                                 play_button, aliens,
                                 bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        if play_button.rect.collidepoint(mouse_x, mouse_y):
            pygame.mouse.set_visible(False)
            stats.reset_stats()
            stats.game_active = True

            aliens.empty()
            bullets.empty()

            create_fleet(ai_settings, screen, ship, aliens)
            ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                  play_button):  # Função responsável pela atualizações de tela no jogo
    screen.fill(ai_settings.background_colour)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb,
                   ship, aliens, bullets):  # Função responsável pela atualizações de projéteis no jogo
    bullets.update()
    for bullet in bullets.copy():  # Verifica se os projéteis saíram da tela
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  # Caso sim, o laço "for" irá apagá-las para que não consuma muita memória
    check_bullets_alien_collisions(ai_settings, screen, ship, stats, sb, aliens, bullets)


def fire_bullets(ai_settings, screen, ship, bullets):  # Função que limitará os projéteis disparados pela espaçonave
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):  #Loop que criará a frota de alienigenas
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2.5 * alien_width  # Limita até onde os alienigenas podem chegar na borda horizontal
    number_alien_x = int(available_space_x / (2.5 * alien_width))  # Calcula quantos alienigenas cabem na tela
    return number_alien_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2.5 * alien_width * alien_number  # Define o espaço entre os alienigenas, no caso o espaço é de 2 alienigenas
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """"Determina o número de linhas de alienigenas que cabem na tela"""
    available_space_y = (ai_settings.screen_height - (2 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)  # Verifica se a frota está em uma borda, então atualiza as posições
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False


def check_fleet_edges(ai_settings, aliens):
    """Verifica se algum alienígena alcançou uma borda"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Faz toda frota descer e muda a direção"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= - 1


def check_bullets_alien_collisions(ai_settings, screen, ship, stats, sb, aliens, bullets):
    """Verifica a colisões entre projéteis e alienígenas"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def start_game_from_key(ai_settings, screen, stats, ship, aliens, bullets):
    if not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def enter_or_exit_full_screen_mode(ai_settings):
    if ai_settings.game_on_full_screen:
        pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        ai_settings.game_on_full_screen = False
    else:
        pygame.display.set_mode((ai_settings.monitor_screen_widht, ai_settings.monitor_screen_height),
                                pygame.FULLSCREEN)
        ai_settings.game_on_full_screen = True
