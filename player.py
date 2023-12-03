import pygame
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface,create_jump_particles):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15  # tells us how fast our animation is going to update
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # dust particles
        self.import_dust_run_particles()
        self.dust_frame_index = 0
        self.dust_animation_speed = 0.15
        self.display_surface = surface
        self.create_jump_particles = create_jump_particles

        # player movement
        # using Vector2 which is a list that contains an X and Y value
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        # negative number for jump so the player jumps up
        self.jump_speed = -16
        # incoperating a double jump
        self.num_jumps = 2
        self.jump_timer = 0

        # player status
        # default status of player is idle
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def import_character_assets(self):
        character_path = 'graphics/character/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            # accesses files inside one folder
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder('graphics/character/dust_particles/run')

    def animate(self):
        # picking specfic key from the self.animations
        animation = self.animations[self.status]

        # loop over frame index, so basically every frame of game you are adding 0.15
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)  # flip x
            self.image = flipped_image

        # set the rectangle on png
        # this is covering all possible collisons with png and level so it doesn't look buggy
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def run_dust_animation(self):
        if self.status == 'run' and self.on_ground:
            self.dust_frame_index += self.dust_animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0

            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

            if self.facing_right:
                # if player moving to right, spawn dust particles at bottom left of player
                pos = self.rect.bottomleft - pygame.math.Vector2(6,10)
                self.display_surface.blit(dust_particle, pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(6, 10)
                flipped_dust_particle = pygame.transform.flip(dust_particle,True,False)
                self.display_surface.blit(flipped_dust_particle,pos)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            # using x because horizontal
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            # same thing but since we are getting keys from left it's going to be negative
            self.direction.x = -1
            self.facing_right = False
        else:
            # not moving at all
            self.direction.x = 0

        if keys[pygame.K_SPACE]:  # player going to only jump if pressing space and on ground
            if self.on_ground or self.num_jumps > 0:
                self.jump()
                self.create_jump_particles(self.rect.midbottom)

    def get_status(self):
        if self.direction.y < 0:  # saying that y direction negative then the status of player is jump
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        # so setting a timer so that everytime you jump, you have to wait 10 frames so you can jump again
        # doing -1 so it doesn't overlap and goes back to 0
        if self.jump_timer <= 0:
            self.jump_timer = 10
            self.direction.y = self.jump_speed
            self.num_jumps -= 1

    def update(self):
        # calling this function
        self.get_input()
        self.get_status()
        self.animate()
        self.run_dust_animation()
        if self.jump_timer > 0:
            self.jump_timer -= 1
