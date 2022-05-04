import pygame
from player import Player
from enemy import Enemy
from sound import Sound



class Game:
    def __init__(self):

        self.is_playing = False

        self.is_over = False    #statut pour afficher image over sur ecran accueil

        self.pressed = {}  # création dictionnaire vide permettant de stocker info de la touche préssée


        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)

        self.enemy = Enemy(self)
        self.all_enemy = pygame.sprite.Group()

        self.all_exploses = pygame.sprite.Group()

        self.score = 0

        self.earth_protection = 500
        self.earth_max_protection = 500





    def start(self):
        self.is_playing = True
        self.spawn_enemy()
        self.music = Sound()

    def update_game(self, screen):

        screen.blit(self.player.image, self.player.rect)

        for projectile in self.player.all_projectiles:
            projectile.move()

        self.player.all_projectiles.draw(screen)

        self.player.update_health_bar(screen)

        self.update_earth_protection_bar(screen)




        self.all_enemy.draw(screen)
        for enemy in self.all_enemy:
            enemy.move()
            enemy.update_health_bar(screen)
            enemy.all_lasers.draw(screen)
            for laser in enemy.all_lasers:
                laser.move()

        for explose in self.all_exploses:
            if explose.animation:
                explose.animate()
            else:
                self.all_exploses.remove(explose)
        self.all_exploses.draw(screen)

        #affichage score ecran de jeu
        font = pygame.font.Font("assets/font/ibm.ttf", 50)
        score_text = font.render(f"{self.score}", 1, (30, 30, 30))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()


    def game_over(self):
        self.all_enemy = pygame.sprite.Group()
        self.player.rect.x = 445
        self.player.rect.y = 600
        self.player.health = 100
        self.is_playing = False
        self.score = 0
        self.earth_protection = 500
        self.is_over = True


    def spawn_enemy(self):
        self.all_enemy.add(Enemy(self))


    def collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)



    def update_earth_protection_bar(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), [10, 10, self.earth_max_protection / 3, 10])
        pygame.draw.rect(surface, (255, 255, 255), [10, 10, self.earth_protection / 3, 10])

    def earth_damage(self, amount):
        self.earth_protection -= amount
        if self.earth_protection <= 0:
            self.game_over()






