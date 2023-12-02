import pygame
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15  # tells us how fast our animation is going to update
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        # using Vector2 which is a list that contains an X and Y value
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        # negative number for jump so the player jumps up
        self.jump_speed = -16

    def import_character_assets(self):
        character_path = 'graphics/character/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            # accesses files inside one folder
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            # using x because horizontal
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            # same thing but since we are getting keys from left it's going to be negative
            self.direction.x = -1
        else:
            # not moving at all
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        # calling this function
        self.get_input()
