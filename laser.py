import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, enemy):
        super().__init__()
        self.image = pygame.image.load("assets/arme/super_laser.png")
        self.image = pygame.transform.scale(self.image, (20, 20))


        self.enemy = enemy
        self.all_enemy = pygame.sprite.Group()

        self.rect = self.image.get_rect()
        self.rect.x = enemy.rect.x + 20
        self.rect.y = enemy.rect.y + 10

        self.attack = 5
        self.velocity = 40

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y >= 600:
            self.remove()
        #collision avec joueur
        for player in self.enemy.game.collision(self, self.enemy.game.all_players):
            self.remove()
            player.damage(self.attack)
        #colision avec projectile
        if self.enemy.game.collision(self, self.enemy.game.player.all_projectiles):
            self.remove()
            self.enemy.game.score += 50




    def remove(self):
        self.enemy.all_lasers.remove(self)
