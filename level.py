import pygame
from tiles import Tile
from settings import tile_size, screen_width
from player import Player


class Level:
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shift = 0

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

                    player_sprite = Player((x, y))
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
                elif player.direction.x > 0:  # checking moving right
                    player.rect.right = sprite.rect.left

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
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
