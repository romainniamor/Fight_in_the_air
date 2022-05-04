import pygame

from projectile import Projectile
from explose import Explose

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load("assets/vehicule/player.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x = 445
        self.rect.y = 600

        self.velocity = 20

        self.health = 100
        self.max_health = 100

        self.game = game

        self.projectile = Projectile(self)
        self.all_projectiles = pygame.sprite.Group()


    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (155, 155, 155), [self.rect.x, self.rect.y + self.rect.height + 10, self.max_health, 4])
        pygame.draw.rect(surface, (0, 0, 0), [self.rect.x, self.rect.y + self.rect.height + 10, self.health , 4])

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.game.all_exploses.add(Explose(self.rect.x, self.rect.y))
            self.game.game_over()

    def update_animation(self):
        self.animate()



