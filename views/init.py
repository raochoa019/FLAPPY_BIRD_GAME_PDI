import pygame
from pygame.locals import *

import sys
from components.Button import Button

class InitView():
    def __init__(self):
        pygame.display.set_caption('Flappy Bird: Proyecto PDI - Beltrán, Ochoa')

        self.screen_res = [640, 480]
        self.screen = pygame.display.set_mode(self.screen_res, pygame.HWSURFACE, 32)
        self.running = False

        while True:
            self.Loop()

    def Loop(self):
        self.eventLoop()
        self.Draw()
        pygame.display.update()

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()

    def Draw(self):
        CENTER_WIDTH, CENTER_HEIGHT = self.screen.get_rect().center

        # Buttons/Rectangles
        btnJugar = Button((118, 191, 20), 250, CENTER_HEIGHT, 150, 50, text="Jugar")
        btnCreditos = Button((118, 191, 20), 230, CENTER_HEIGHT + 80, 180, 50, text="Creditos")
        btnDIP = Button((255, 255, 255), 30, 435, 240, 30, text="DIP 2022-PAO2", sizeText=15)
        btnDevelopers = Button((255, 255, 255), 340, 435, 270, 30, text="Beltran - Ochoa", sizeText=15)

        # Images
        imgLogo = pygame.image.load('./imgs/Flappy_Logo.png').convert_alpha()
        imgLogo = pygame.transform.scale(imgLogo, (400, 100))

        imgBird = pygame.image.load('./imgs/bird_sprite.png').convert_alpha()
        imgBird = pygame.transform.scale(imgBird, (75, 50))

        # Fill the background with cian
        self.screen.fill((0, 199, 218))

        # Place buttons
        btnJugar.draw(self.screen)
        btnCreditos.draw(self.screen)
        btnDIP.draw(self.screen)
        btnDevelopers.draw(self.screen)

        # Place images
        self.screen.blit(imgLogo, imgLogo.get_rect(center=(CENTER_WIDTH, 80)))
        self.screen.blit(imgBird, imgBird.get_rect(center=(CENTER_WIDTH, 160)))
