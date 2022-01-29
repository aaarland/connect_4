from Board import Board
from Colors import *
from Player import Player
import pygame
from pygame.locals import *

class Game:
    def __init__(self, width, height, fps) -> None:
        self.width = width
        self.height = height
        self._display_surf = None
        self._running = True
        self.fps = fps
        self.mouse_clicked = False
        self.next_player = Player(RED)
        self.prev_player = Player(YELLOW)
        self.time_counter = 0


    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.width, self.height))
        self._running = True
        self.frames_per_sec = pygame.time.Clock()
        self.board = Board(self._display_surf)
        
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        if event.type == MOUSEBUTTONDOWN:
            self.mouse_clicked = True

    def on_cleanup(self):
        pygame.quit()
    
    def on_loop(self):
        if self.mouse_clicked:
            self.mouse_clicked = False
            self.board.add_chip(self.next_player)
            self.next_player, self.prev_player = self.prev_player, self.next_player
        if self.time_counter >= 200:
            self.time_counter = 0
            self.board.fall_chips()
        if self.board.is_won((self.prev_player, self.next_player)):
            print(self.board.winner)


    def on_render(self):
        self._display_surf.fill(BLUE)
        self.board.draw()

    def start_game(self) -> None:
        if self.on_init() == False:
            self._running = False
        while (self._running):
            pygame.display.update()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.time_counter += self.frames_per_sec.tick(self.fps)
        self.on_cleanup
        pass
