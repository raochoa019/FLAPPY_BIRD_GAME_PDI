import pygame
from pygame.locals import *

import sys
from components.Button import Button

class InitView():
    def __init__(self, window_size):
        pygame.display.set_caption('Flappy Bird: Proyecto PDI - Beltrán, Ochoa')
        self.window_size = window_size
        self.screen = pygame.display.set_mode(self.window_size)
        self.running = False

        # Buttons/Rectangles
        self.__btnJugar = None
        self.__btnCreditos = None
        self.__btnDIP = None
        self.__btnDevelopers = None

        # Images
        self.__imgLogo = None
        self.__imgBird = None

        self.__initializeComponents()

    def show(self):
        self.running = True
        while self.running:
            self.loop()

    def loop(self):
        self.eventLoop()
        self.draw()
        pygame.display.update()

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    def draw(self):
        # Fill the background with cian
        self.screen.fill((0, 199, 218))
        CENTER_WIDTH, CENTER_HEIGHT = self.screen.get_rect().center

        # Place buttons
        self.__btnJugar.draw(self.screen)
        self.__btnCreditos.draw(self.screen)
        self.__btnDIP.draw(self.screen)
        self.__btnDevelopers.draw(self.screen)

        # Place images
        self.screen.blit(self.__imgLogo, self.__imgLogo.get_rect(center=(CENTER_WIDTH, 80)))
        self.screen.blit(self.__imgBird, self.__imgBird.get_rect(center=(CENTER_WIDTH, 160)))

    # Button's functions
    def __pressPlayButton(self):
        print("Jugar")

    def __pressCreditsButton(self):
        print("Creditos")

    # Initialize interface's components
    def __initializeComponents(self):
        CENTER_WIDTH, CENTER_HEIGHT = self.screen.get_rect().center

        # Initialize Buttons/Rectangles
        self.__btnJugar = Button((118, 191, 20), 250, CENTER_HEIGHT, 150, 50, text="Jugar",
                                 onClickFunction=self.__pressPlayButton)
        self.__btnCreditos = Button((118, 191, 20), 230, CENTER_HEIGHT + 80, 180, 50, text="Creditos",
                                    onClickFunction=self.__pressCreditsButton)
        self.__btnDIP = Button((255, 255, 255), 30, 435, 240, 30, text="DIP 2022-PAO2", sizeText=15)
        self.__btnDevelopers = Button((255, 255, 255), 340, 435, 270, 30, text="Beltran - Ochoa", sizeText=15)

        # Initialize images
        self.__imgLogo = pygame.image.load('./imgs/Flappy_Logo.png').convert_alpha()
        self.__imgLogo = pygame.transform.scale(self.__imgLogo, (400, 100))

        self.__imgBird = pygame.image.load('./imgs/bird_sprite.png').convert_alpha()
        self.__imgBird = pygame.transform.scale(self.__imgBird, (75, 50))