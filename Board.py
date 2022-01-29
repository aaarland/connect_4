
import pygame
from pygame.locals import *
from Chip import Chip
from Colors import *

class Board:
    def __init__(self, display_surf) -> None:
        self.chips = [[None for i in range(7)] for j in range(5)]
        h, w = pygame.display.get_surface().get_size()
        self.width = w
        self.height = h
        self.ball_width = (w / 7) / 2 + 3.6
        self._display_surf = display_surf
        self.fps_counter = 0
        self._create_chips()
        self.winner = None

    def _create_chips(self):
        for i in range(5):
            for j in range(7):
                chip = Chip(self. _display_surf, (j * (self.ball_width + 5) * 2) + self.ball_width, 
                (i * (self.ball_width + 5) * 2) + self.ball_width, 
                WHITE, self.ball_width)
                self.chips[i][j] = chip
    
    def add_chip(self, player):
        x, y = pygame.mouse.get_pos()
        for row in self.chips:
            for chip in row:
                if x <= chip.x + self.ball_width \
                    and x >= chip.x - self.ball_width \
                    and y <= chip.y + self.ball_width \
                    and y >= chip.y - self.ball_width \
                    and y <= self.ball_width * 2:
                        chip.color = player.color

    def fall_chips(self):
        chip_index = []
        for i, row in enumerate(self.chips):
            for j, chip in enumerate(row):
                if (chip.color == RED or chip.color == YELLOW)\
                    and i + 1 < len(self.chips) \
                    and self.chips[i + 1][j].color == WHITE:
                        chip_index.append((i, j))

        for i, j in chip_index:
            self.chips[i + 1][j].color = self.chips[i][j].color
            self.chips[i][j].color = WHITE


    def _check_horizontal(self, players):
        for i, row in enumerate(self.chips):
            for j, chip in enumerate(row):
                if j + 4 < len(row):
                    if chip.color != WHITE \
                        and chip.color == self.chips[i][j + 1].color \
                        and chip.color == self.chips[i][j + 2].color \
                        and chip.color == self.chips[i][j + 3].color:
                        self._set_winner(players, chip)
                        return True
        return False
    def _set_winner(self, players, chip):
        if chip.color == players[0].color:
            self.winner = players[0]
        else:
            self.winner = players[1]

    def _check_vertical(self, players):
        for i, row in enumerate(self.chips):
            for j, chip in enumerate(row):
                if i + 4 < len(self.chips):
                    if chip.color != WHITE \
                        and chip.color == self.chips[i + 1][j].color \
                        and chip.color == self.chips[i + 2][j].color \
                        and chip.color == self.chips[i + 3][j].color:
                        self._set_winner(players, chip)
                        return True
        return False

    def _check_cross(self, players):
        for i, row in enumerate(self.chips):
            for j, chip in enumerate(row):
                if i + 4 < len(self.chips) and j + 4 < len(row):
                    if chip.color != WHITE \
                        and chip.color == self.chips[i + 1][j + 1].color \
                        and chip.color == self.chips[i + 2][j + 2].color \
                        and chip.color == self.chips[i + 3][j + 3].color:
                        self._set_winner(players, chip)
                        return True
                if i + 4 < len(self.chips) and j - 4 >= 0:
                    if chip.color != WHITE \
                        and chip.color == self.chips[i + 1][j - 1].color \
                        and chip.color == self.chips[i + 2][j - 2].color \
                        and chip.color == self.chips[i + 3][j - 3].color:
                        self._set_winner(players, chip)
                        return True
        return False

    
    def is_won(self, players):
        return self._check_horizontal(players) or self._check_vertical(players)


    def draw(self):
        for row in self.chips:
            for chip in row:
                chip.draw()

