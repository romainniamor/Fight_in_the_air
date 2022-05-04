import pygame
from game import Game


pygame.init()
game = Game()


clock = pygame.time.Clock()
pygame.display.set_caption("Sky Fight")

screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load("assets/game/background.png")
background = pygame.transform.scale(background, (1080, 720))

banner = pygame.image.load("assets/game/banner.png")
banner = pygame.transform.scale(banner, (550, 720))

over = pygame.image.load("assets/game/game-over.png")
over = pygame.transform.scale(over, (150, 150))
over = pygame.transform.rotate(over, 12)

message1 = "The earth is in danger"
message2 = "Protect her"
message3 = "Don't be killed"
message4 = "Press Space to shoot"
message5 = "Press F to FIGHT!"
message6 = "MISSION FAILED"
message7 = "Press F to Restart"
font = pygame.font.Font("assets/font/ibm.ttf", 30)
message_text1 = font.render(message1, 1, (30, 30, 30))
message_text2 = font.render(message2, 1, (30, 30, 30))
message_text3 = font.render(message3, 1, (30, 30, 30))
message_text4 = font.render(message4, 1, (30, 30, 30))
message_text5 = font.render(message5, 1, (30, 30, 30))
message_text6 = font.render(message6, 1, (30, 30, 30))
message_text7 = font.render(message7, 1, (30, 30, 30))


running = True


while running:
    clock.tick(30)
    screen.blit(background, (0, 0))


    if game.is_playing:
        game.update_game(screen)
    else:
        if game.is_over:
            screen.fill((255, 255, 255))
            screen.blit(banner, (0,0))
            screen.blit(over, (160, 100))
            screen.blit(message_text6, (550, 210))
            screen.blit(message_text7, (550, 300))
        else:
            screen.fill((255, 255, 255))
            screen.blit(banner, (0, 0))
            screen.blit(message_text1, (550, 150))
            screen.blit(message_text2, (550, 180))
            screen.blit(message_text3, (550, 210))
            screen.blit(message_text4, (550, 260))
            screen.blit(message_text5, (550, 330))

        pygame.display.flip()


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            if event.key == pygame.K_f:
                game.start()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
    if game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height + 20 < screen.get_height():
        game.player.move_down()

