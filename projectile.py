import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load("assets/arme/bullet.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

        self.player = player
        self.rect.x = player.rect.x + 40
        self.rect.y = player.rect.y - 20

        self.velocity = 70
        self.attack = 55

    def move(self):
        self.rect.y -= self.velocity
        if self.rect.y == 10:
            self.remove()
        #colision avec enemi
        for enemy in self.player.game.collision(self, self.player.game.all_enemy):
            self.remove()
            enemy.damage(self.attack)
            self.player.game.score += 3

    def remove(self):
        self.player.all_projectiles.remove(self)