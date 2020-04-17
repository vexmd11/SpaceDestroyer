# ~~~~~~~~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~~~~~~~~~ #


def main_menu():

    # Load sprites
    title = pygame.image.load("spacedestroyer.png")
    play = pygame.image.load("play.png")
    instructions = pygame.image.load("instructions.png")
    quit_image = pygame.image.load("quit.png")
    spaceship_menu = pygame.image.load("spaceship_menu.png")
    enemy_menu = pygame.image.load("enemy_menu.png")
    health_menu = pygame.image.load("health_menu.png")
    sound = pygame.image.load("sound.png")
    sound_off = pygame.image.load("sound off.png")

    # Define rects (hitbox)
    sound_rect = pygame.Rect(750, 550, 32, 32)
    mute_rect = pygame.Rect(-100, -100, 32, 32)
    play_rect = pygame.Rect(250, 250, 300, 75)
    instructions_rect = pygame.Rect(250, 350, 300, 75)
    quit_rect = pygame.Rect(250, 450, 300, 75)

    while True:

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Checking for collision using mouse clicks
            elif event.type == MOUSEBUTTONDOWN:
                if play_rect.collidepoint(pygame.mouse.get_pos()):
                    gamemode()
                elif instructions_rect.collidepoint(pygame.mouse.get_pos()):
                    show_instructions()
                elif quit_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                elif sound_rect.collidepoint(pygame.mouse.get_pos()):
                    sound_rect = pygame.Rect(-100, -100, 32, 32)
                    pygame.mixer.music.set_volume(0)
                    mute_rect = pygame.Rect(750, 550, 32, 32)
                elif mute_rect.collidepoint(pygame.mouse.get_pos()):
                    mute_rect = pygame.Rect(-100, -100, 32, 32)
                    pygame.mixer.music.set_volume(1)
                    sound_rect = pygame.Rect(750, 550, 32, 32)

        # Game state changes
        screen.fill((0, 0, 0))

        # Draw background of screen
        x_pos = 0
        y_pos = 0
        bg_tile = pygame.image.load("background.png")
        for i in range(0, 8):
            for index in range(0, 10):
                screen.blit(bg_tile, (x_pos, y_pos))
                x_pos += 80
            y_pos += 80
            x_pos = 0

        # Draw main menu art
        screen.blit(title, (175, 50))
        screen.blit(spaceship_menu, (5, 300))
        screen.blit(enemy_menu, (555, 0))
        screen.blit(health_menu, (50, 10))

        # Draw buttons on main menu (and hitbox)
        play_rect = pygame.draw.rect(screen, (128, 128, 128), (250, 250, 300, 75), 10)
        instructions_rect = pygame.draw.rect(screen, (128, 128, 128), (250, 350, 300, 75), 10)
        quit_rect = pygame.draw.rect(screen, (128, 128, 128), (250, 450, 300, 75), 10)
        play_rect_2 = pygame.draw.rect(screen, (0, 0, 0), (255, 255, 290, 65))
        instructions_rect_2 = pygame.draw.rect(screen, (0, 0, 0), (255, 355, 290, 65))
        quit_rect_2 = pygame.draw.rect(screen, (0, 0, 0), (255, 455, 290, 65))
        pygame.draw.rect(screen, (255, 0, 0), (245/2, 230, 10, 40))

        # If player hovers over menu option it will light up
        if play_rect_2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (100, 100, 100), (255, 255, 290, 65))
        elif instructions_rect_2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (100, 100, 100), (255, 355, 290, 65))
        elif quit_rect_2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (100, 100, 100), (255, 455, 290, 65))

        # Draw the menu select options, and sound button
        screen.blit(play, (340, 237))
        screen.blit(instructions, (263, 355))
        screen.blit(quit_image, (340, 453))
        screen.blit(sound, sound_rect)
        screen.blit(sound_off, mute_rect)

        # Update display
        pygame.display.update()

# ~~~~~~~~~~~~~~~~~~ INSTRUCTIONS PG 2 ~~~~~~~~~~~~~~~~~~ #


def show_instructions_2():
    global TITLE_FONT

    # Load sprites
    max_ammo = pygame.image.load("max ammo (1).png")
    enemy = pygame.image.load("enemy.png")
    heart = pygame.image.load("heart (1).png")
    back = pygame.image.load("back.png")
    boss = pygame.image.load("boss(1).png")

    # Text for instructions page
    ammo_text = TITLE_FONT.render("You have limited ammo, so collect these for a", True, (255, 255, 255))
    ammo_text_2 = TITLE_FONT.render("refill!", True, (255, 255, 255))
    enemy_text = TITLE_FONT.render("Kill enemies to gain one ammo and 10 points!", True, (255, 255, 255))
    enemy_text_2 = TITLE_FONT.render("Don't let them slip by or you lose points!", True, (255, 255, 255))
    heart_text = TITLE_FONT.render("You also have limited hearts!", True, (255, 255, 255))
    heart_text_2 = TITLE_FONT.render("Lose all of them and it's GAME OVER!", True, (255, 255, 255))
    boss_text = TITLE_FONT.render("Reach 2000 score and fight the Boss!", True, (255, 255, 255))

    # Hitbox for back arrow
    back_rect = pygame.Rect(600, 525, 75, 75)

    # Colours
    grey = (128, 128, 128)

    while True:
        clock.tick(60)

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Checking for collision using mouse clicks
            elif event.type == MOUSEBUTTONDOWN:
                if back_rect.collidepoint(pygame.mouse.get_pos()):
                    return

        # Game state changes
        screen.fill((0, 0, 0))

        # Draw background of screen
        x_pos = 0
        y_pos = 0
        bg_tile = pygame.image.load("background.png")
        for i in range(0, 8):
            for index in range(0, 10):
                screen.blit(bg_tile, (x_pos, y_pos))
                x_pos += 80
            y_pos += 80
            x_pos = 0

        # Draw sprites and text on instructions screen
        screen.blit(max_ammo, (50, 30))
        pygame.draw.rect(screen, (0, 0, 0), (110, 30, 700, 80))
        screen.blit(ammo_text, (120, 30))
        screen.blit(ammo_text_2, (120, 70))
        screen.blit(enemy, (50, 160))
        pygame.draw.rect(screen, (0, 0, 0), (110, 160, 700, 80))
        screen.blit(enemy_text, (120, 160))
        screen.blit(enemy_text_2, (120, 200))
        screen.blit(heart, (50, 290))
        pygame.draw.rect(screen, (0, 0, 0), (110, 290, 600, 80))
        screen.blit(heart_text, (120, 290))
        screen.blit(heart_text_2, (120, 330))
        screen.blit(back, back_rect)
        screen.blit(boss, (15, 420))
        pygame.draw.rect(screen, (0, 0, 0), (110, 420, 550, 40))
        screen.blit(boss_text, (120, 420))

        # Back arrow rect will change colour if player hovers over it
        pygame.draw.rect(screen, grey, back_rect, 5)
        if back_rect.collidepoint(pygame.mouse.get_pos()):
            grey = (255, 255, 255)
        else:
            grey = (128, 128, 128)

        # update display
        pygame.display.update()

# ~~~~~~~~~~~~~~~~~~ INSTRUCTIONS ~~~~~~~~~~~~~~~~~~ #


def show_instructions():
    global TITLE_FONT

    # Colours
    grey = (128, 128, 128)
    grey2 = (128, 128, 128)

    # Load sprites
    up = pygame.image.load("up.png")
    left = pygame.image.load("left.png")
    right = pygame.image.load("right.png")
    down = pygame.image.load("down.png")
    space = pygame.image.load("space.png")
    instructions = pygame.image.load("instructions.png")
    score_powerup = pygame.image.load("doublepoints (1).png")
    health_powerup = pygame.image.load("health (1).png")
    speed_powerup = pygame.image.load("speed (1).png")
    back_image = pygame.image.load("back.png")
    next_image = pygame.image.load("next.png")
    back_rect = pygame.Rect(600, 525, 75, 75)
    next_rect = pygame.Rect(700, 525, 75, 75)

    # Text for instructions screen
    up_text = TITLE_FONT.render("Move up", True, (255, 255, 255))
    down_text = TITLE_FONT.render("Move down", True, (255, 255, 255))
    left_text = TITLE_FONT.render("Move left", True, (255, 255, 255))
    right_text = TITLE_FONT.render("Move right", True, (255, 255, 255))
    space_text = TITLE_FONT.render("Shoot lasers", True, (255, 255, 255))
    health_text = TITLE_FONT.render("Collect it for +1 HP", True, (255, 255, 255))
    score_text = TITLE_FONT.render("Collect it for double", True, (255, 255, 255))
    score_text_2 = TITLE_FONT.render("score, for a small", True, (255, 255, 255))
    score_text_3 = TITLE_FONT.render("amount of time", True, (255, 255, 255))
    speed_text = TITLE_FONT.render("Collect it for a speed", True, (255, 255, 255))
    speed_text_2 = TITLE_FONT.render("boost, for a small", True, (255, 255, 255))
    speed_text_3 = TITLE_FONT.render("amount of time", True, (255, 255, 255))

    while True:
        clock.tick(60)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Checking for collision using mouse clicks
            elif event.type == MOUSEBUTTONDOWN:
                if back_rect.collidepoint(pygame.mouse.get_pos()):
                    return
                elif next_rect.collidepoint(pygame.mouse.get_pos()):
                    show_instructions_2()

        # Game state changes
        screen.fill((255, 0, 0))

        # Draw background on screen
        x_pos = 0
        y_pos = 0
        bg_tile = pygame.image.load("background.png")
        for i in range(0, 8):
            for index in range(0, 10):
                screen.blit(bg_tile, (x_pos, y_pos))
                x_pos += 80
            y_pos += 80
            x_pos = 0

        # Draw sprites and text on instructions screen
        screen.blit(instructions, (50, 30))
        screen.blit(up, (50, 120))
        pygame.draw.rect(screen, (0, 0, 0), (110, 120, 140, 50))
        screen.blit(up_text, (120, 120))
        screen.blit(down, (50, 210))
        pygame.draw.rect(screen, (0, 0, 0), (110, 210, 185, 50))
        screen.blit(down_text, (120, 210))
        screen.blit(left, (50, 300))
        pygame.draw.rect(screen, (0, 0, 0), (110, 300, 150, 50))
        screen.blit(left_text, (120, 300))
        screen.blit(right, (50, 390))
        pygame.draw.rect(screen, (0, 0, 0), (110, 390, 185, 50))
        screen.blit(right_text, (120, 390))
        screen.blit(space, (50, 480))
        pygame.draw.rect(screen, (0, 0, 0), (110, 480, 200, 50))
        screen.blit(space_text, (120, 480))
        screen.blit(health_powerup, (400, 120))
        pygame.draw.rect(screen, (0, 0, 0), (460, 120, 325, 50))
        screen.blit(health_text, (470, 120))
        screen.blit(score_powerup, (400, 210))
        pygame.draw.rect(screen, (0, 0, 0), (460, 210, 325, 125))
        screen.blit(score_text, (470, 210))
        screen.blit(score_text_2, (470, 250))
        screen.blit(score_text_3, (470, 290))
        screen.blit(speed_powerup, (400, 380))
        pygame.draw.rect(screen, (0, 0, 0), (460, 380, 325, 125))
        screen.blit(speed_text, (470, 380))
        screen.blit(speed_text_2, (470, 420))
        screen.blit(speed_text_3, (470, 460))
        screen.blit(back_image, back_rect)
        screen.blit(next_image, next_rect)

        # Back and next arrow rects will change colour if player hovers over
        pygame.draw.rect(screen, grey, back_rect, 5)
        if back_rect.collidepoint(pygame.mouse.get_pos()):
            grey = (255, 255, 255)
        else:
            grey = (128, 128, 128)

        pygame.draw.rect(screen, grey2, next_rect, 5)
        if next_rect.collidepoint(pygame.mouse.get_pos()):
            grey2 = (255, 255, 255)
        else:
            grey2 = (128, 128, 128)

        # Update display
        pygame.display.update()

# ~~~~~~~~~~~~~~~~~~ WIN SCREEN ~~~~~~~~~~~~~~~~~~ #


def win_screen():

    # Set text and load images
    win_text = pygame.image.load("you_win.png")
    score_text = TITLE_FONT.render(str(score), True, (255, 255, 255))
    message1 = TITLE_FONT.render("You won with a score of:", True, (255, 255, 255))
    message2 = TITLE_FONT.render("points", True, (255, 255, 255))
    message3 = TITLE_FONT.render("Press 'ESC' to return to menu", True, (255, 255, 255))

    while True:
        clock.tick(60)  # refers to 60fps

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Escape brings you back to main menu
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()

        # Game changes
        screen.fill((0, 0, 0))

        # Gradient Background
        colour_var = 0
        line_y = 0
        black = (0 + colour_var, 0 + colour_var, 0 + colour_var)
        for i in range(0, 510):
            pygame.draw.line(screen, black, (0, line_y), (800, line_y), 2)
            black = (0, 0, 0 + colour_var)
            colour_var += 0.5
            line_y += 2

        # Draw text
        screen.blit(win_text, (215, 100))
        screen.blit(message1, (235, 300))
        screen.blit(score_text, (380, 350))
        screen.blit(message2, (370, 400))
        screen.blit(message3, (175, 500))

        pygame.display.update()

# ~~~~~~~~~~~~~~~~~~ DEATH SCREEN ~~~~~~~~~~~~~~~~~~ #


def death_screen():

    # Text to make up seconds death screen
    gameover_text = pygame.image.load("gameover.png")
    score_text = TITLE_FONT.render(str(round(score, 1)), True, (255, 255, 255))
    message1 = TITLE_FONT.render("Your score is:", True, (255, 255, 255))
    message2 = TITLE_FONT.render("points", True, (255, 255, 255))
    message3 = TITLE_FONT.render("Press 'ESC' to return to menu", True, (255, 255, 255))

    while True:
        clock.tick(60)  # refers to 60fps

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Escape bring you back to menu
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()

        # Game changes
        screen.fill((0, 0, 0))

        # Gradient Background
        colour_var = 0
        line_y = 0
        black = (0 + colour_var, 0 + colour_var, 0 + colour_var)
        for i in range(0, 510):
            pygame.draw.line(screen, black, (0, line_y), (800, line_y), 2)
            black = (0 + colour_var, 0, 0)
            colour_var += 0.5
            line_y += 2

        # Draw text on death screen
        screen.blit(gameover_text, (145, 100))
        screen.blit(message1, (300, 300))
        screen.blit(score_text, (370, 350))
        screen.blit(message2, (355, 400))
        screen.blit(message3, (175, 500))

        pygame.display.update()

    # Update display
    pygame.display.update()

# ~~~~~~~~~~~~~~~~~~ CHOOSE GAMEMODE ~~~~~~~~~~~~~~~~~~ #
import pygame
pygame.init()

# Set Font
TITLE_FONT = pygame.font.SysFont("perpetua", 40)

# Load sprites
endless_image = pygame.image.load("endless.png")
withboss_image = pygame.image.load("withboss.png")
hardcore_image = pygame.image.load("hardcore.png")

# Set rects (hitbox)
bossgame_rect = pygame.Rect(200, 100, 400, 100)
endlessgame_rect = pygame.Rect(200, 250, 400, 100)
hardcoregame_rect = pygame.Rect(200, 400, 400, 100)

# Text messages
hardcore_text = TITLE_FONT.render("[Don't let enemies hit the ground!]", True, (255, 0, 0))


def gamemode():

    while True:
        clock.tick(60)  # refers to 60fps

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Escape brings you back to menu
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            # Collision using mouse clicks
            elif event.type == MOUSEBUTTONDOWN:
                if bossgame_rect.collidepoint(pygame.mouse.get_pos()):
                    play_game()
                elif endlessgame_rect.collidepoint(pygame.mouse.get_pos()):
                    endless()
                elif hardcoregame_rect.collidepoint(pygame.mouse.get_pos()):
                    hardcore()

        # Game changes
        screen.fill((0, 0, 0))

        # Draw Background
        x_pos = 0
        y_pos = 0
        bg_tile = pygame.image.load("background.png")
        for i in range(0, 8):
            for index in range(0, 10):
                screen.blit(bg_tile, (x_pos, y_pos))
                x_pos += 80
            y_pos += 80
            x_pos = 0

        # Draw gamemode options and hitboxes
        pygame.draw.rect(screen, (128, 128, 128), bossgame_rect, 10)
        pygame.draw.rect(screen, (128, 128, 128), endlessgame_rect, 10)
        pygame.draw.rect(screen, (128, 128, 128), hardcoregame_rect, 10)
        pygame.draw.rect(screen, (0, 0, 0), (205, 105, 390, 90))
        pygame.draw.rect(screen, (0, 0, 0), (205, 255, 390, 90))
        pygame.draw.rect(screen, (0, 0, 0), (205, 405, 390, 90))
        pygame.draw.rect(screen, (0, 0, 0), (145, 510, 530, 50))

        # If player hovers over menu option it will light up
        if bossgame_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (100, 100, 100), (205, 105, 390, 90))
        elif endlessgame_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (100, 100, 100), (205, 255, 390, 90))
        elif hardcoregame_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (100, 100, 100), (205, 405, 390, 90))

        # Draw text on boxes
        screen.blit(withboss_image, (225, 105))
        screen.blit(endless_image, (260, 255))
        screen.blit(hardcore_image, (235, 405))
        screen.blit(hardcore_text, (150, 510))

        pygame.display.update()

# ~~~~~~~~~~~~~~~~~~ HARDCORE GAME ~~~~~~~~~~~~~~~~~~ #


def hardcore():
    global score

    # Define variables
    x = 50
    y = 550
    dx = 0
    dy = 0
    projectile_dy = -5
    enemy_y = 0
    enemy_dy = 3
    loops = 0
    loops_health = 0
    loops_score = 0
    loops_speed = 0
    loops_ammo = 0
    loops_damage = 0
    hp = 3
    score = 0
    points = 10
    speed = 0
    ammo = 20

    enemies = []  # List to hold all enemies
    projectiles = []  # List to hold all projectiles

    # Load sprites
    player_sprite = pygame.image.load("spaceship.png")
    enemy_sprite = pygame.image.load("enemy.png")
    heart_sprite = pygame.image.load("heart.png")
    score_powerup = pygame.image.load("doublepoints.png")
    health_powerup = pygame.image.load("health.png")
    speed_powerup = pygame.image.load("speed.png")
    max_ammo = pygame.image.load("Max ammo.png")
    damage_heart = pygame.image.load("damage_heart.png")
    sound = pygame.image.load("sound.png")
    sound_off = pygame.image.load("sound off.png")

    # Set rects for hitboxes
    health_rect = pygame.Rect(-100, -100, 32, 32)
    score_rect = pygame.Rect(-100, -100, 32, 32)
    speed_rect = pygame.Rect(-100, -100, 32, 32)
    ammo_rect = pygame.Rect(-100, -100, 32, 32)
    sound_rect = pygame.Rect(750, 550, 32, 32)
    mute_rect = pygame.Rect(-100, -100, 32, 32)

    while True:

        clock.tick(60)  # Refers to 60fps

        # Redefine enemy x and player hitbox
        enemy_x = random.randrange(0, 750)  # Redefine random x location
        player_rect = pygame.Rect(x, y, 50, 50)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Actions using arrow keys to move, and space to shoot
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    dx -= 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_RIGHT:
                    dx += 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_UP:
                    dy -= 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_DOWN:
                    dy += 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_SPACE:
                    if ammo == 0:
                        break
                    elif ammo != 0:
                        projectiles.append([pygame.Rect(x + 25, y, 5, 9), projectile_dy])  # Add projectile to list
                        ammo -= 1
                elif event.key == K_i:
                    show_instructions()  # i key shows instructions in game
            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    dx = 0
                    player_sprite = pygame.image.load("spaceship.png")
                elif event.key == K_UP or event.key == K_DOWN:
                    dy = 0
                    player_sprite = pygame.image.load("spaceship.png")
            # Collision using mouse clicks for the mute button
            elif event.type == MOUSEBUTTONDOWN:
                if sound_rect.collidepoint(pygame.mouse.get_pos()):
                    sound_rect = pygame.Rect(-100, -100, 32, 32)
                    pygame.mixer.music.set_volume(0)
                    mute_rect = pygame.Rect(750, 550, 32, 32)
                elif mute_rect.collidepoint(pygame.mouse.get_pos()):
                    mute_rect = pygame.Rect(-100, -100, 32, 32)
                    pygame.mixer.music.set_volume(1)
                    sound_rect = pygame.Rect(750, 550, 32, 32)

        # Change x by dx, and y by dy
        x += dx
        y += dy

        # If player steps out of boundaries, sprite will be set at these x and y coordinates
        if x > 800:
            x = 0
        if x < 0:
            x = 800
        if y > 600:
            y = 500
        if y < 0:
            y = 500

        # Game state changes
        screen.fill((0, 0, 0))

        # Draw Background
        x_pos = 0
        y_pos = 0
        bg_tile = pygame.image.load("background.png")
        for i in range(0, 8):
            for index in range(0, 10):
                screen.blit(bg_tile, (x_pos, y_pos))
                x_pos += 80
            y_pos += 80
            x_pos = 0

        # Draw sound icon
        screen.blit(sound, sound_rect)
        screen.blit(sound_off, mute_rect)

        # Draw player on screen, on hitbox
        screen.blit(player_sprite, player_rect)

        # Remove projectiles past a certain point
        for projectile in projectiles:
            if projectile[0].y < 0:
                projectiles.remove(projectile)

        # Move projectiles by a certain speed
        for projectile in projectiles:
            projectile[1] += 1
            projectile[0].move_ip(0, projectile_dy)

        # Draw projectiles on screen
        for projectile in projectiles:
            pygame.draw.rect(screen, (255, 0, 0), projectile[0])

        # Draw enemies on screen
        for enemy in enemies:
            screen.blit(enemy_sprite, enemy[0])

        # Moves enemies
        for enemy in enemies:
            enemy[1] += 1
            enemy[0].move_ip(0, enemy_dy)

        # If enemy touches bottom, game over!
        for enemy in enemies:
            if enemy[0].y >= 600:
                death_screen()
                enemies.remove(enemy)

        # Lose 1 HP if enemy collides with player
        for enemy in enemies:
            if enemy[0].colliderect(player_rect):
                enemies.remove(enemy)
                hp -= 1
                loops_damage = 100
                if hp == 0:
                    death_screen()  # If player's HP = 0, GAME OVER
        if loops_damage > 0:
            screen.blit(damage_heart, (x + 25, y - 20))  # Draw a damage heart near the player, to know they took damage
            loops_damage -= 1
        elif loops_damage == 0:
            loops_damage = 0

        # Collision to check if projectiles hit an enemy
        for enemy in enemies:
            for projectile in projectiles:
                if projectile[0].colliderect(enemy[0]):
                    projectiles.remove(projectile)
                    enemies.remove(enemy)
                    score += points
                    ammo += 1
                    break

        # Collision with health powerup, adds 1 hp
        if player_rect.colliderect(health_rect):
            health_rect = (pygame.Rect(-100, -100, 32, 32))  # Move rect off screen, player can't collide with it again
            hp += 1
            loops_health = 0

        # Collision with score powerup, double score for small amount of time
        if player_rect.colliderect(score_rect):
            score_rect = pygame.Rect(-100, -100, 32, 32)  # Move rect off screen, player can't collide with it again
            points = 20
            loops_score = 0

        # Collision with speed powerup, speed boost for small amount of time
        if player_rect.colliderect(speed_rect):
            speed_rect = pygame.Rect(-100, -100, 32, 32)  # Move rect off screen, player can't collide with it again
            speed = 3
            loops_speed = 0

        # Collision with max ammo, give max ammo (20)
        if player_rect.colliderect(ammo_rect):
            ammo_rect = pygame.Rect(-100, -100, 32, 32)  # Move rect off screen, player can't collide with it again
            ammo = 20
            loops_ammo = 0

        # For every 70 loops (less than one second) spawns a new enemy
        loops += 1
        if loops == 70:
            enemies.append([pygame.draw.rect(screen, (255, 255, 255), (enemy_x, enemy_y, 50, 50)), enemy_dy])
            loops = 0

        # Every 2000 loops spawn a health powerup
        if loops_health != 2000:
            loops_health += 1
        elif loops_health == 2000:
            health_rect = pygame.Rect(400, 400, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(health_powerup, health_rect)

        # Every 4000 loops spawn a score powerup
        if loops_score != 4000:
            loops_score += 1
        if loops_score == 1500:  # Set points back to 10 after loops_score == 1500
            points = 10
            loops_score += 1
        elif loops_score == 4000:
            score_rect = pygame.Rect(200, 400, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(score_powerup, score_rect)

        # Every 4000 loops spawn a max ammo
        if loops_ammo != 4000:
            loops_ammo += 1
        elif loops_ammo == 4000:
            ammo_rect = pygame.Rect(400, 500, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(max_ammo, ammo_rect)

        # Every 6000 loops spawn a speed powerup
        if loops_speed != 6000:
            loops_speed += 1
        if loops_speed == 2000:
            speed = 0  # Set speed back to 0 after loops_speed == 2000
            loops_speed += 1
        elif loops_speed == 6000:
            speed_rect = pygame.Rect(600, 400, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(speed_powerup, speed_rect)

        # Show the score at top right corner
        score_int = TITLE_FONT.render(str(score), True, (255, 255, 255))
        score_text = TITLE_FONT.render("Score: ", True, (255, 255, 255))
        screen.blit(score_text, (600, 10))
        screen.blit(score_int, (700, 10))

        # Show health at top left corner
        health_int = TITLE_FONT.render(str(hp), True, (255, 255, 255))
        health_text = TITLE_FONT.render("x ", True, (255, 255, 255))
        screen.blit(heart_sprite, (35, 15))
        screen.blit(health_text, (80, 10))
        screen.blit(health_int, (100, 10))

        # Show ammo at bottom left
        ammo_text = TITLE_FONT.render("Ammo: ", True, (255, 255, 255))
        ammo_int = TITLE_FONT.render(str(ammo), True, (255, 255, 255))
        screen.blit(ammo_text, (10, 550))
        screen.blit(ammo_int, (125, 550))

        # Update display
        pygame.display.update()

# ~~~~~~~~~~~~~~~~~~ ENDLESS GAME ~~~~~~~~~~~~~~~~~~ #


def endless():
    global score

    # Define variables
    x = 50
    y = 550
    dx = 0
    dy = 0
    projectile_dy = -5
    enemy_y = 0
    enemy_dy = 3
    loops = 0
    loops_health = 0
    loops_score = 0
    loops_speed = 0
    loops_ammo = 0
    loops_damage = 0
    hp = 3
    score = 0
    points = 10
    speed = 0
    ammo = 20

    enemies = []  # List to hold all enemies
    projectiles = []  # List to hold all projectiles

    # Load sprites
    player_sprite = pygame.image.load("spaceship.png")
    enemy_sprite = pygame.image.load("enemy.png")
    heart_sprite = pygame.image.load("heart.png")
    score_powerup = pygame.image.load("doublepoints.png")
    health_powerup = pygame.image.load("health.png")
    speed_powerup = pygame.image.load("speed.png")
    max_ammo = pygame.image.load("Max ammo.png")
    damage_heart = pygame.image.load("damage_heart.png")
    sound = pygame.image.load("sound.png")
    sound_off = pygame.image.load("sound off.png")

    # Set rects (hitboxes)
    health_rect = pygame.Rect(-100, -100, 32, 32)
    score_rect = pygame.Rect(-100, -100, 32, 32)
    speed_rect = pygame.Rect(-100, -100, 32, 32)
    ammo_rect = pygame.Rect(-100, -100, 32, 32)
    sound_rect = pygame.Rect(750, 550, 32, 32)
    mute_rect = pygame.Rect(-100, -100, 32, 32)

    while True:

        clock.tick(60)  # Refers to 60fps

        # Redefine enemy x and player rect
        enemy_x = random.randrange(0, 750)  # Redefine random x location
        player_rect = pygame.Rect(x, y, 50, 50)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Actions to move player using arrow keys
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    dx -= 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_RIGHT:
                    dx += 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_UP:
                    dy -= 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_DOWN:
                    dy += 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                # Space used to shoot laser
                elif event.key == K_SPACE:
                    if ammo == 0:
                        break
                    elif ammo != 0:
                        projectiles.append([pygame.Rect(x + 25, y, 5, 9), projectile_dy])
                        ammo -= 1
                elif event.key == K_i:
                    show_instructions()  # i key shows instructions in game
            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    dx = 0
                    player_sprite = pygame.image.load("spaceship.png")
                elif event.key == K_UP or event.key == K_DOWN:
                    dy = 0
                    player_sprite = pygame.image.load("spaceship.png")
            # Collision using mouse clicks with mute button
            elif event.type == MOUSEBUTTONDOWN:
                if sound_rect.collidepoint(pygame.mouse.get_pos()):
                    sound_rect = pygame.Rect(-100, -100, 32, 32)
                    pygame.mixer.music.set_volume(0)
                    mute_rect = pygame.Rect(750, 550, 32, 32)
                elif mute_rect.collidepoint(pygame.mouse.get_pos()):
                    mute_rect = pygame.Rect(-100, -100, 32, 32)
                    pygame.mixer.music.set_volume(1)
                    sound_rect = pygame.Rect(750, 550, 32, 32)

        # Change x by dx, and y by dy
        x += dx
        y += dy

        # If player steps out of boundaries, sprite will be set at these x and y coordinates
        if x > 800:
            x = 0
        if x < 0:
            x = 800
        if y > 600:
            y = 500
        if y < 0:
            y = 500

        # Game state changes
        screen.fill((0, 0, 0))

        # Draw Background
        x_pos = 0
        y_pos = 0
        bg_tile = pygame.image.load("background.png")
        for i in range(0, 8):
            for index in range(0, 10):
                screen.blit(bg_tile, (x_pos, y_pos))
                x_pos += 80
            y_pos += 80
            x_pos = 0

        # Draw sound icon
        screen.blit(sound, sound_rect)
        screen.blit(sound_off, mute_rect)

        # Draw player on screen, on hitbox
        screen.blit(player_sprite, player_rect)

        # Remove projectiles past a certain point
        for projectile in projectiles:
            if projectile[0].y < 0:
                projectiles.remove(projectile)

        # Move projectiles by a certain speed
        for projectile in projectiles:
            projectile[1] += 1
            projectile[0].move_ip(0, projectile_dy)

        # Draw projectiles on screen
        for projectile in projectiles:
            pygame.draw.rect(screen, (255, 0, 0), projectile[0])

        # Draw enemies on screen
        for enemy in enemies:
            screen.blit(enemy_sprite, enemy[0])

        # Moves enemies
        for enemy in enemies:
            enemy[1] += 1
            enemy[0].move_ip(0, enemy_dy)

        # Destroy enemies past a certain point
        for enemy in enemies:
            if enemy[0].y > 600:
                if score > 0:
                    score -= 10  # If enemy reaches bottom, -10 score
                elif score == 0:
                    score -= 0
                enemies.remove(enemy)

        # Lose 1 HP if enemy collides with player
        for enemy in enemies:
            if enemy[0].colliderect(player_rect):
                enemies.remove(enemy)
                hp -= 1
                loops_damage = 100
                if hp == 0:
                    death_screen()  # If hp = 0, GAME OVER
        if loops_damage > 0:
            screen.blit(damage_heart, (x + 25, y - 20))  # Draw damage heart near player, to know they took damage
            loops_damage -= 1
        elif loops_damage == 0:
            loops_damage = 0

        # Collision to check if projectiles hit an enemy
        for enemy in enemies:
            for projectile in projectiles:
                if projectile[0].colliderect(enemy[0]):
                    projectiles.remove(projectile)
                    enemies.remove(enemy)
                    score += points
                    ammo += 1
                    break

        # Collision with health powerup
        if player_rect.colliderect(health_rect):
            health_rect = (pygame.Rect(-100, -100, 32, 32))  # Move rect off screen, player can't collide with it again
            hp += 1
            loops_health = 0

        # Collision with score powerup
        if player_rect.colliderect(score_rect):
            score_rect = pygame.Rect(-100, -100, 32, 32)  # Move rect off screen, player can't collide with it again
            points = 20
            loops_score = 0

        # Collision with speed powerup
        if player_rect.colliderect(speed_rect):
            speed_rect = pygame.Rect(-100, -100, 32, 32)  # Move rect off screen, player can't collide with it again
            speed = 3
            loops_speed = 0

        # Collision with max ammo
        if player_rect.colliderect(ammo_rect):
            ammo_rect = pygame.Rect(-100, -100, 32, 32)  # Move rect off screen, player can't collide with it again
            ammo = 20
            loops_ammo = 0

        # For every 70 loops (less than a second) spawns a new enemy
        loops += 1
        if loops == 70:
            enemies.append([pygame.draw.rect(screen, (255, 255, 255), (enemy_x, enemy_y, 50, 50)), enemy_dy])
            loops = 0

        # Every 2000 loops spawn a health powerup, give player 1 HP
        if loops_health != 2000:
            loops_health += 1
        elif loops_health == 2000:
            health_rect = pygame.Rect(400, 400, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(health_powerup, health_rect)

        # Every 4000 loops spawn a score powerup, double score for small amount of time
        if loops_score != 4000:
            loops_score += 1
        if loops_score == 1500:  # Set points back to 10 after loops_score == 1500
            points = 10
            loops_score += 1
        elif loops_score == 4000:
            score_rect = pygame.Rect(200, 400, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(score_powerup, score_rect)

        # Every 4000 loops spawn a max ammo, gives player max ammo (20)
        if loops_ammo != 4000:
            loops_ammo += 1
        elif loops_ammo == 4000:
            ammo_rect = pygame.Rect(400, 500, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(max_ammo, ammo_rect)

        # Every 6000 loops spawn a speed powerup, speed boost for small amount of time
        if loops_speed != 6000:
            loops_speed += 1
        if loops_speed == 2000:
            speed = 0  # Set speed back to 0 after loops_speed == 2000
            loops_speed += 1
        elif loops_speed == 6000:
            speed_rect = pygame.Rect(600, 400, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(speed_powerup, speed_rect)

        # Show the score at top right corner
        score_int = TITLE_FONT.render(str(score), True, (255, 255, 255))
        score_text = TITLE_FONT.render("Score: ", True, (255, 255, 255))
        screen.blit(score_text, (600, 10))
        screen.blit(score_int, (700, 10))

        # Show health at top left corner
        health_int = TITLE_FONT.render(str(hp), True, (255, 255, 255))
        health_text = TITLE_FONT.render("x ", True, (255, 255, 255))
        screen.blit(heart_sprite, (35, 15))
        screen.blit(health_text, (80, 10))
        screen.blit(health_int, (100, 10))

        # Show ammo at bottom left
        ammo_text = TITLE_FONT.render("Ammo: ", True, (255, 255, 255))
        ammo_int = TITLE_FONT.render(str(ammo), True, (255, 255, 255))
        screen.blit(ammo_text, (10, 550))
        screen.blit(ammo_int, (125, 550))

        pygame.display.update()

# ~~~~~~~~~~~~~~~~~~ BOSS FIGHT ~~~~~~~~~~~~~~~~~~ #


def boss_fight():
    global score

    # Define variables
    x = 50
    y = 550
    dx = 0
    dy = 0
    boss_x = 100
    boss_y = -500
    boss_dx = 3
    boss_health_bar_y = 200
    boss_health_bar_height = 200
    projectile_dy = -5
    boss_projectile_dy = 8
    loops_health = 0
    loops_speed = 0
    loops_ammo = 0
    loops_damage = 0
    loops_laser = 0
    hp = 3
    boss_hp = 100
    score = 2000
    speed = 0
    ammo = 20

    projectiles = []  # List to hold all projectiles
    boss_projectiles = []

    # Load sprites
    player_sprite = pygame.image.load("spaceship.png")
    heart_sprite = pygame.image.load("heart.png")
    health_powerup = pygame.image.load("health.png")
    speed_powerup = pygame.image.load("speed.png")
    max_ammo = pygame.image.load("Max ammo.png")
    damage_heart = pygame.image.load("damage_heart.png")
    boss = pygame.image.load("boss.png")
    sound = pygame.image.load("sound.png")
    sound_off = pygame.image.load("sound off.png")

    # Set rects (hitbox)
    health_rect = pygame.Rect(-100, -100, 32, 32)
    speed_rect = pygame.Rect(-100, -100, 32, 32)
    ammo_rect = pygame.Rect(-100, -100, 32, 32)
    boss_rect = pygame.Rect(boss_x, boss_y, 600, 200)
    sound_rect = pygame.Rect(750, 550, 32, 32)
    mute_rect = pygame.Rect(-100, -100, 32, 32)

    while True:

        clock.tick(60)  # Refers to 60fps

        # Redefine player hitbox
        player_rect = pygame.Rect(x, y, 50, 50)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Actions using arrow keys to move
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    dx -= 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_RIGHT:
                    dx += 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_UP:
                    dy -= 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_DOWN:
                    dy += 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                # Space shoots laser
                elif event.key == K_SPACE:
                    if ammo == 0:
                        break
                    elif ammo != 0:
                        projectiles.append([pygame.Rect(x + 25, y, 5, 9), projectile_dy])
                        ammo -= 1
                elif event.key == K_i:
                    show_instructions()  # i key shows instructions in game
            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    dx = 0
                    player_sprite = pygame.image.load("spaceship.png")
                elif event.key == K_UP or event.key == K_DOWN:
                    dy = 0
                    player_sprite = pygame.image.load("spaceship.png")
            # Mouse clicks for collision with mute button
            elif event.type == MOUSEBUTTONDOWN:
                if sound_rect.collidepoint(pygame.mouse.get_pos()):
                    sound_rect = pygame.Rect(-100, -100, 32, 32)
                    pygame.mixer.music.set_volume(0)
                    mute_rect = pygame.Rect(750, 550, 32, 32)
                elif mute_rect.collidepoint(pygame.mouse.get_pos()):
                    mute_rect = pygame.Rect(-100, -100, 32, 32)
                    pygame.mixer.music.set_volume(1)
                    sound_rect = pygame.Rect(750, 550, 32, 32)

        # Change x by dx, and y by dy
        x += dx
        y += dy

        # Boss will change directions at these x coordinates
        if boss_x >= 350:
            boss_dx = -3
        elif boss_x <= -150:
            boss_dx = 3

        # Boss moves in on screen
        if boss_y < 10:
            boss_rect.move_ip(0, 2)
            boss_y += 2
        elif boss_y == 10:
            boss_y = 10  # Boss stops when y = 10
            boss_rect.move_ip(boss_dx, 0)
            boss_x += boss_dx

        # If player steps out of boundaries, player will be set at these x and y coords
        if x > 800:
            x = 0
        if x < 0:
            x = 800
        if y > 600:
            y = 500
        if y < 250:
            y = 500

        # Game state changes
        screen.fill((0, 0, 0))

        # Draw Background
        x_pos = 0
        y_pos = 0
        bg_tile = pygame.image.load("background.png")
        for i in range(0, 8):
            for index in range(0, 10):
                screen.blit(bg_tile, (x_pos, y_pos))
                x_pos += 80
            y_pos += 80
            x_pos = 0

        # Draw boss, health bar and hitbox
        screen.blit(boss, boss_rect)
        boss_health_bar = (50, boss_health_bar_y, 20, boss_health_bar_height)
        pygame.draw.rect(screen, (255, 0, 0), (50, 200, 20, 200))
        pygame.draw.rect(screen, (0, 255, 0), boss_health_bar)

        # Draw sound icon
        screen.blit(sound, sound_rect)
        screen.blit(sound_off, mute_rect)

        # Draw player on screen, on hitbox
        screen.blit(player_sprite, player_rect)

        # Remove projectiles past a certain point
        for projectile in projectiles:
            if projectile[0].y < 0:
                projectiles.remove(projectile)

        # Move projectiles by a certain speed
        for projectile in projectiles:
            projectile[1] += 1
            projectile[0].move_ip(0, projectile_dy)

        # Draw projectiles on screen
        for projectile in projectiles:
            pygame.draw.rect(screen, (255, 0, 0), projectile[0])

        # Draw boss projectiles
        for projectile in boss_projectiles:
            pygame.draw.rect(screen, (255, 0, 0), projectile[0])

        # Move boss projectiles
        for projectile in boss_projectiles:
            projectile[1] += 1
            projectile[0].move_ip(0, boss_projectile_dy)

        # Remove projectiles past certain point
        for projectile in boss_projectiles:
            if projectile[0].y > 600:
                boss_projectiles.remove(projectile)

        # Boss shoots lasers every 75 loops(less than 1 second)
        loops_laser += 1
        if loops_laser == 175:
            boss_projectiles.append([pygame.Rect(boss_x + 200, 180, 8, 12), boss_projectile_dy])
            boss_projectiles.append([pygame.Rect(boss_x + 400, 180, 8, 12), boss_projectile_dy])
            loops_laser = 100

        # Collision to check if projectiles hits boss
        for projectile in projectiles:
            if projectile[0].colliderect(boss_rect):
                projectiles.remove(projectile)
                boss_health_bar_y += 2
                boss_health_bar_height -= 2
                boss_hp -= 1
                if boss_hp == 0:  # If boss hp = 0, YOU WIN
                    win_screen()
                break

        # Collision to check if projectiles hit player
        for projectile in boss_projectiles:
            if projectile[0].colliderect(player_rect):
                boss_projectiles.remove(projectile)
                hp -= 1
                loops_damage = 100
                if hp == 0:
                    death_screen()  # If player hp = 0, GAME OVER
        if loops_damage > 0:
            screen.blit(damage_heart, (x + 25, y - 20))  # Draw damage heart near player, to know they took damage
            loops_damage -= 1
        elif loops_damage == 0:
            loops_damage = 0

        # Collision with health powerup, gives player 1 HP
        if player_rect.colliderect(health_rect):
            health_rect = (pygame.Rect(-100, -100, 32, 32))  # Move rect off screen, player can't collide with it again
            hp += 1
            loops_health = 0

        # Collision with speed powerup, speed boost for small amount of time
        if player_rect.colliderect(speed_rect):
            speed_rect = pygame.Rect(-100, -100, 32, 32)  # Move rect off screen, player can't collide with it again
            speed = 3
            loops_speed = 0

        # Collision with max ammo, gives max ammo (20)
        if player_rect.colliderect(ammo_rect):
            ammo_rect = pygame.Rect(-100, -100, 32, 32)  # Move rect off screen, player can't collide with it again
            ammo = 20
            loops_ammo = 0

        # Every 2000 loops spawn a health powerup
        if loops_health != 2000:
            loops_health += 1
        elif loops_health == 2000:
            health_rect = pygame.Rect(400, 400, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(health_powerup, health_rect)

        # Every 1500 loops spawn a max ammo
        if loops_ammo != 1500:
            loops_ammo += 1
        elif loops_ammo == 1500:
            ammo_rect = pygame.Rect(200, 400, 32, 32)   # Move rect on screen so player can collide with it
            screen.blit(max_ammo, ammo_rect)

        # Every 3000 loops spawn a speed powerup
        if loops_speed != 3000:
            loops_speed += 1
        if loops_speed == 2000:
            speed = 0  # Set speed back to 0 after loops_speed == 2000
            loops_speed += 1
        elif loops_speed == 3000:
            speed_rect = pygame.Rect(600, 400, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(speed_powerup, speed_rect)

        # Show the score at top right corner
        score_int = TITLE_FONT.render(str(score), True, (255, 255, 255))
        score_text = TITLE_FONT.render("Score: ", True, (255, 255, 255))
        screen.blit(score_text, (600, 10))
        screen.blit(score_int, (700, 10))

        # Show health at top left corner
        health_int = TITLE_FONT.render(str(hp), True, (255, 255, 255))
        health_text = TITLE_FONT.render("x ", True, (255, 255, 255))
        screen.blit(heart_sprite, (35, 15))
        screen.blit(health_text, (80, 10))
        screen.blit(health_int, (100, 10))

        # Show ammo at bottom left
        ammo_text = TITLE_FONT.render("Ammo: ", True, (255, 255, 255))
        ammo_int = TITLE_FONT.render(str(ammo), True, (255, 255, 255))
        screen.blit(ammo_text, (10, 550))
        screen.blit(ammo_int, (125, 550))

        # Update display
        pygame.display.update()

# ~~~~~~~~~~~~~~~~~~ PLAY GAME ~~~~~~~~~~~~~~~~~~ #


def play_game():
    global score

    # Define variables
    x = 50
    y = 550
    dx = 0
    dy = 0
    projectile_dy = -5
    enemy_y = 0
    enemy_dy = 3
    loops = 0
    loops_health = 0
    loops_score = 0
    loops_speed = 0
    loops_ammo = 0
    loops_damage = 0
    hp = 3
    score = 0
    points = 10
    speed = 0
    ammo = 20

    enemies = []  # List to hold all enemies
    projectiles = []  # List to hold all projectiles

    # Load sprites
    player_sprite = pygame.image.load("spaceship.png")
    enemy_sprite = pygame.image.load("enemy.png")
    heart_sprite = pygame.image.load("heart.png")
    score_powerup = pygame.image.load("doublepoints.png")
    health_powerup = pygame.image.load("health.png")
    speed_powerup = pygame.image.load("speed.png")
    max_ammo = pygame.image.load("Max ammo.png")
    damage_heart = pygame.image.load("damage_heart.png")
    sound = pygame.image.load("sound.png")
    sound_off = pygame.image.load("sound off.png")

    # Set rects (hitbox)
    health_rect = pygame.Rect(-100, -100, 32, 32)
    score_rect = pygame.Rect(-100, -100, 32, 32)
    speed_rect = pygame.Rect(-100, -100, 32, 32)
    ammo_rect = pygame.Rect(-100, -100, 32, 32)
    sound_rect = pygame.Rect(750, 550, 32, 32)
    mute_rect = pygame.Rect(-100, -100, 32, 32)

    while True:

        clock.tick(60)  # Refers to 60fps

        # Redefine enemy x and player hitbox
        enemy_x = random.randrange(0, 750)  # Redefine random x location
        player_rect = pygame.Rect(x, y, 50, 50)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Actions using arrow keys to move player
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    dx -= 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_RIGHT:
                    dx += 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_UP:
                    dy -= 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                elif event.key == K_DOWN:
                    dy += 5 + speed
                    player_sprite = pygame.image.load("spaceship_moving.png")
                # Space shoots lasers
                elif event.key == K_SPACE:
                    if ammo == 0:
                        break
                    elif ammo != 0:
                        projectiles.append([pygame.Rect(x + 25, y, 5, 9), projectile_dy])  # Adds projectile to list
                        ammo -= 1
                elif event.key == K_i:
                    show_instructions()  # i key shows instructions in game
            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    dx = 0
                    player_sprite = pygame.image.load("spaceship.png")
                elif event.key == K_UP or event.key == K_DOWN:
                    dy = 0
                    player_sprite = pygame.image.load("spaceship.png")
            # Mouse clicks for collision with mute button
            elif event.type == MOUSEBUTTONDOWN:
                if sound_rect.collidepoint(pygame.mouse.get_pos()):
                    sound_rect = pygame.Rect(-100, -100, 32, 32)
                    pygame.mixer.music.set_volume(0)
                    mute_rect = pygame.Rect(750, 550, 32, 32)
                elif mute_rect.collidepoint(pygame.mouse.get_pos()):
                    mute_rect = pygame.Rect(-100, -100, 32, 32)
                    pygame.mixer.music.set_volume(1)
                    sound_rect = pygame.Rect(750, 550, 32, 32)

        # Change x by dx, and y by dy
        x += dx
        y += dy

        # If player steps out of boundaries, sprite will be set at these x and y coordinates
        if x > 800:
            x = 0
        if x < 0:
            x = 800
        if y > 600:
            y = 500
        if y < 0:
            y = 500

        # Game state changes
        screen.fill((0, 0, 0))

        # Draw Background
        x_pos = 0
        y_pos = 0
        bg_tile = pygame.image.load("background.png")
        for i in range(0, 8):
            for index in range(0, 10):
                screen.blit(bg_tile, (x_pos, y_pos))
                x_pos += 80
            y_pos += 80
            x_pos = 0

        # Draw sound icon
        screen.blit(sound, sound_rect)
        screen.blit(sound_off, mute_rect)

        # Draw player on screen, on hitbox
        screen.blit(player_sprite, player_rect)

        # Remove projectiles past a certain point
        for projectile in projectiles:
            if projectile[0].y < 0:
                projectiles.remove(projectile)

        # Move projectiles by a certain speed
        for projectile in projectiles:
            projectile[1] += 1
            projectile[0].move_ip(0, projectile_dy)

        # Draw projectiles on screen
        for projectile in projectiles:
            pygame.draw.rect(screen, (255, 0, 0), projectile[0])

        # Draw enemies on screen
        for enemy in enemies:
            screen.blit(enemy_sprite, enemy[0])

        # Moves enemies
        for enemy in enemies:
            enemy[1] += 1
            enemy[0].move_ip(0, enemy_dy)

        # Destroy enemies past a certain point
        for enemy in enemies:
            if enemy[0].y > 600:
                if score > 0:
                    score -= 10  # If enemy reaches bottom, -10 score
                elif score == 0:
                    score -= 0
                enemies.remove(enemy)

        # Lose 1 HP if enemy collides with player
        for enemy in enemies:
            if enemy[0].colliderect(player_rect):
                enemies.remove(enemy)
                hp -= 1
                loops_damage = 100
                if hp == 0:
                    death_screen()  # If players hp = 0, GAME OVER
        if loops_damage > 0:
            screen.blit(damage_heart, (x + 25, y - 20))  # Draws damage heart near player to know they took damage
            loops_damage -= 1
        elif loops_damage == 0:
            loops_damage = 0

        # Collision to check if projectiles hit an enemy
        for enemy in enemies:
            for projectile in projectiles:
                if projectile[0].colliderect(enemy[0]):
                    projectiles.remove(projectile)
                    enemies.remove(enemy)
                    score += points
                    ammo += 1
                    break

        # Collision with health powerup, adds 1 HP
        if player_rect.colliderect(health_rect):
            health_rect = (pygame.Rect(-100, -100, 32, 32))  # Move rect off screen, player can't collide with it again
            hp += 1
            loops_health = 0

        # Collision with score powerup, double score for small amount of time
        if player_rect.colliderect(score_rect):
            score_rect = pygame.Rect(-100, -100, 32, 32)  # Move rect off screen, player can't collide with it again
            points = 20
            loops_score = 0

        # Collision with speed powerup, speed boost for small amount of time
        if player_rect.colliderect(speed_rect):
            speed_rect = pygame.Rect(-100, -100, 32, 32)  # Move rect off screen, player can't collide with it again
            speed = 3
            loops_speed = 0

        # Collision with max ammo, gives player max ammo (20)
        if player_rect.colliderect(ammo_rect):
            ammo_rect = pygame.Rect(-100, -100, 32, 32)  # Move rect off screen, player can't collide with it again
            ammo = 20
            loops_ammo = 0

        # For every 90 loops (one second or so) spawns a new enemy
        loops += 1
        if loops == 90:
            enemies.append([pygame.draw.rect(screen, (255, 255, 255), (enemy_x, enemy_y, 50, 50)), enemy_dy])
            loops = 0

        # Every 2000 loops spawn a health powerup
        if loops_health != 2000:
            loops_health += 1
        elif loops_health == 2000:
            health_rect = pygame.Rect(400, 400, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(health_powerup, health_rect)

        # Every 4000 loops spawn a score powerup
        if loops_score != 4000:
            loops_score += 1
        if loops_score == 1500:  # Set points back to 10 after loops_score == 1500
            points = 10
            loops_score += 1
        elif loops_score == 4000:
            score_rect = pygame.Rect(200, 400, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(score_powerup, score_rect)

        # Every 4000 loops spawn a max ammo
        if loops_ammo != 4000:
            loops_ammo += 1
        elif loops_ammo == 4000:
            ammo_rect = pygame.Rect(400, 500, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(max_ammo, ammo_rect)

        # Every 6000 loops spawn a speed powerup
        if loops_speed != 6000:
            loops_speed += 1
        if loops_speed == 2000:
            speed = 0  # Set speed back to 0 after loops_speed == 2000
            loops_speed += 1
        elif loops_speed == 6000:
            speed_rect = pygame.Rect(600, 400, 32, 32)  # Move rect on screen so player can collide with it
            screen.blit(speed_powerup, speed_rect)

        # Show the score at top right corner
        score_int = TITLE_FONT.render(str(score), True, (255, 255, 255))
        score_text = TITLE_FONT.render("Score: ", True, (255, 255, 255))
        screen.blit(score_text, (600, 10))
        screen.blit(score_int, (700, 10))

        # Show health at top left corner
        health_int = TITLE_FONT.render(str(hp), True, (255, 255, 255))
        health_text = TITLE_FONT.render("x ", True, (255, 255, 255))
        screen.blit(heart_sprite, (35, 15))
        screen.blit(health_text, (80, 10))
        screen.blit(health_int, (100, 10))

        # Show ammo at bottom left
        ammo_text = TITLE_FONT.render("Ammo: ", True, (255, 255, 255))
        ammo_int = TITLE_FONT.render(str(ammo), True, (255, 255, 255))
        screen.blit(ammo_text, (10, 550))
        screen.blit(ammo_int, (125, 550))

        if score >= 2000:  # Boss fight when score >= 2000
            boss_fight()

        # Update display
        pygame.display.update()

# ~~~~~~~~~~~~~~~~~~~ START GAME ~~~~~~~~~~~~~~~~~~~ #
import pygame
import sys
import random
from pygame.locals import *
pygame.init()  # init() means initialize

# Set screen and clock
screen = pygame.display.set_mode((800, 600))  # Display 800x600
clock = pygame.time.Clock()

# Set font
TITLE_FONT = pygame.font.SysFont("perpetua", 40)

# Load game music, volume, loops
pygame.mixer.music.load("spacemusic.mp3")
pygame.mixer.music.play(loops=-1, start=0.0)
pygame.mixer.music.set_volume(1)

# Start at main menu
main_menu()