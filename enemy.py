import pygame
from laser import Laser
from random import randint
from explose import Explose

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load("assets/vehicule/vessel.png")
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.rect = self.image.get_rect()
        self.rect.x = randint(10, 900)
        self.rect.y = - randint(0, 10)

        self.velocity = randint(1, 6)

        self.attack = 25

        self.health = 100
        self.max_health = 100

        self.laser = Laser(self)
        self.all_lasers = pygame.sprite.Group()

        self.game = game

        self.objective_x = randint(0, (1080 - self.rect.width))
        self.objective_y = randint(0, 750)


    '''#basic move
    def move(self):
        if self.rect.y < 720:
            self.rect.y += self.velocity
            for player in self.game.collision(self, self.game.all_players):
                self.game.all_exploses.add(Explose(self.rect.x, self.rect.y))
                self.remove()
                self.game.score += 10
                player.damage(self.attack)
            if self.rect.y == randint(0, 175):
                self.launch_laser()
        else:
            self.remove()
            self.game.earth_damage(self.attack)'''


    def move(self):
        for player in self.game.collision(self, self.game.all_players):
            self.game.all_exploses.add(Explose(self.rect.x, self.rect.y))
            self.remove()
            self.game.score += 10
            player.damage(self.attack)
        if self.rect.y > 720:
            self.remove()
            self.game.earth_damage(self.attack)
        if self.rect.x < self.objective_x:
            self.rect.x += self.velocity
        elif self.rect.x > self.objective_x:
            self.rect.x -= self.velocity
        if abs(self.rect.x - self.objective_x) < self.velocity:
            self.objective_x = randint(0, (1080 - self.rect.width))
            self.launch_laser()
        if self.rect.y < self.objective_y:
            self.rect.y += self.velocity
        elif self.rect.y > self.objective_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.objective_y) < self.velocity:
            self.objective_y = randint(0, 780)
            self.launch_laser()


    def remove(self):
        self.rect.x = randint(10, 900)
        self.rect.y = - randint(30, 50)
        self.health = self.max_health

    def launch_laser(self):
        self.all_lasers.add(Laser(self))

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (165, 165, 165), [self.rect.x + 5, self.rect.y - 4, self.max_health / 2, 2])
        pygame.draw.rect(surface, (0, 0, 0), [self.rect.x + 5, self.rect.y - 4, self.health / 2, 2])

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.score += 15
            self.game.all_exploses.add(Explose(self.rect.x, self.rect.y))
            self.remove()
            self.game.spawn_enemy()




