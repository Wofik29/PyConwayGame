import pygame

import constants
from Game import Game


class Window:
    def __init__(self) -> None:
        self.tickCount = 0
        self.sc = None
        self.game = None
        self.game_quit = False
        self.game_init()

    def game_init(self):
        pygame.init()
        self.game = Game()
        self.sc = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))
        pygame.display.set_caption(constants.GAME_TITLE)

    def run(self):
        self.render()
        clock = pygame.time.Clock()

        while not self.game_quit:
            clock.tick(60)
            self.tickCount += 1
            self.render()

            if self.tickCount == 10:
                self.tick()
                self.tickCount = 0

            self.input()

        # quit the game
        pygame.quit()
        exit()

    def render(self):
        pygame.display.flip()

        width = round(constants.GAME_WIDTH / constants.CELL_WIDTH)
        height = round(constants.GAME_HEIGHT / constants.CELL_WIDTH)
        for numberX in range(width - 1):
            for numberY in range(height - 1):
                color = constants.colors.get('light_ground') if self.game.cells[numberX][
                    numberY] else constants.colors.get('dark_ground')

                pygame.draw.rect(self.sc, color, (
                    numberX * constants.CELL_WIDTH, numberY * constants.CELL_WIDTH, constants.CELL_WIDTH,
                    constants.CELL_WIDTH))
                pygame.draw.rect(self.sc, constants.COLOR_GREY, (
                    numberX * constants.CELL_WIDTH, numberY * constants.CELL_WIDTH, constants.CELL_WIDTH,
                    constants.CELL_WIDTH), 1)

    def tick(self):
        self.game.step()

    def input(self):
        events_list = pygame.event.get()
        for event in events_list:
            if event.type == pygame.QUIT:
                self.game_quit = True
