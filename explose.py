import pygame

class Explose(pygame.sprite.Sprite):
    def __init__(self, rect_x, rect_y):
        super().__init__()
        self.image = pygame.image.load("assets/explose/explose1.png")
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

        self.current_image = 0
        self.animation = True
        self.images = animations.get("explose")

    def animate(self, loop=False):
        if self.animation:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False
            self.image = self.images[self.current_image]



def load_animation_images():
        #création d'une liste
    images = []
    path = "assets/explose/explose"

    for num in range(1,8):
        image_path = path + str(num) + ".png"
        img = pygame.image.load(image_path)
        img_scale = pygame.transform.scale(img, (100, 100))
        images.append(img_scale)

    return images

animations = {"explose" : load_animation_images()
              }