import pygame

class Sound:

    def __init__(self):

        self.music = pygame.mixer.music.load("assets/sound/Danger_Zone.mp3")
        self.music_volume = pygame.mixer.music.set_volume(0.05)
        self.music_play = pygame.mixer.music.play(loops=-1)


        """  son a modifier

        self.projectille_sound = pygame.mixer.Sound("assets/sound/gun.mp3")
        self.projectille_sound_volume = pygame.mixer.music.set_volume(0.01)

        self.explose_sound = pygame.mixer.Sound("assets/sound/explosion.mp3")
        self.explose_sound_volume = pygame.mixer.music.set_volume(0.001)"""
