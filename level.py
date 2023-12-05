import pygame
from tiles import Tile
from settings import tile_size, screen_width, max_level_width, level_maps
from player import Player
from particles import ParticleEffect
import random

class Level:
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0

        self.current_level_x = 0

        # dust
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

    def create_jump_particles(self, pos):
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10, 5)
        else:
            pos += pygame.math.Vector2(10, -5)
        jump_particle_sprite = ParticleEffect(pos, 'jump')
        self.dust_sprite.add(jump_particle_sprite)

    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else: # we know player is in the air
            self.player_on_ground = False

    def create_landing_dust(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
            if self.player.sprite.facing_right:
                offset = pygame.math.Vector2(10, 15)
            else:
                offset = pygame.math.Vector2(-10, 15)
            fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset, 'land')
            self.dust_sprite.add(fall_dust_particle)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':

                    player_sprite = Player((x, y),self.display_surface,self.create_jump_particles)
                    self.player.add(player_sprite)

    def scroll_x(self):
        # where player is
        player = self.player.sprite
        # where player is on x coordinate
        player_x = player.rect.centerx
        # what direction player is going to move in
        direction_x = player.direction.x

        # takes care of left side of screen
        # using screen_width from settings so if the screen size changes, the code changes with it
        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
            # takes care of right side of screen
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        # multiplying with self.speed, can update speed of player with function
        player.rect.x += player.direction.x * player.speed  # applying hori movement

        for sprite in self.tiles.sprites():
            # colliderect has access to rectangles of each tile
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:  # checking if our player is moving left
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:  # checking moving right
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    # self.current_x checks what the collison point is
                    self.current_x = player.rect.right
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            # colliderect has access to rectangles of each tile
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    # this handles the constant increase in gravity so player doesn't phase through tiles
                    player.direction.y = 0
                    # so when player is on ground they are allowed 2 jumps
                    player.on_ground = True
                    player.num_jumps = 2
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                    # checking once player on floor and jumping/falling, then the player can no longer be on the floor
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def run(self):
        # dust particles
        self.current_level_x += self.world_shift

        self.dust_sprite.update(self.world_shift)
        self.dust_sprite.draw(self.display_surface)

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.get_player_on_ground()
        self.vertical_movement_collision()
        self.create_landing_dust()
        self.player.draw(self.display_surface)

        # so this is how the level resets, and it choses a random map to set our play to, once player reaches the max level width it resets
        if self.current_level_x <= -max_level_width:
            self.tiles.empty()
            self.setup_level(level_maps[random.randint(0,len(level_maps) - 1)])
            self.world_shift = 0
            self.current_x = 0
            self.current_level_x = 0



