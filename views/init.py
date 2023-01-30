import pygame
from components.Button import Button

class InitView():
    def __init__(self, screen):
        self.screen = screen
        self.__timer = 0

        # Buttons/Rectangles
        self.__btnJugar = None
        self.__btnCreditos = None
        self.__btnDIP = None
        self.__btnDevelopers = None

        # Images
        self.__imgLogo = None
        self.__imgBird = None
        self.__imgBackground = None
        self.__birdIsDown = False
        self.__birdY = 190

        self.__initializeComponents()

    def show(self):
        self.draw()

    def draw(self):
        # Fill the background with cian
        self.screen.fill((0, 199, 218))
        self.screen.blit(self.__imgBackground, (0,0))
        CENTER_WIDTH, CENTER_HEIGHT = self.screen.get_rect().center

        # Place buttons
        self.__btnJugar.draw(self.screen)
        self.__btnCreditos.draw(self.screen)
        self.__btnDIP.draw(self.screen)
        self.__btnDevelopers.draw(self.screen)

        # Place images
        self.__birdY = 170 if self.__birdIsDown else 190
        self.screen.blit(self.__imgLogo, self.__imgLogo.get_rect(center=(CENTER_WIDTH, 80)))
        self.screen.blit(self.__imgBird, self.__imgBird.get_rect(center=(CENTER_WIDTH, self.__birdY)))
        self.__animateBird()

    def __animateBird(self):
        if self.__timer == 200:
            self.__timer = 0
            if self.__birdIsDown:
                self.__birdIsDown = False
            else:
                self.__birdIsDown = True

        self.__timer += 1

    # Button's functions
    def __btnJugar_Click(self):
        with open("config.txt", 'w') as f:
            f.write('2')
        f.close()

    def __btnCreditos_Click(self):
        with open("config.txt", 'w') as f:
            f.write('1')
        f.close()

    # Initialize interface's components
    def __initializeComponents(self):
        CENTER_WIDTH, CENTER_HEIGHT = self.screen.get_rect().center

        # Initialize Buttons/Rectangles
        self.__btnJugar = Button((118, 191, 20), 250, CENTER_HEIGHT, 150, 50, text="Jugar",
                                 onClickFunction=self.__btnJugar_Click)
        self.__btnCreditos = Button((118, 191, 20), 230, CENTER_HEIGHT + 80, 180, 50, text="Creditos",
                                    onClickFunction=self.__btnCreditos_Click)
        self.__btnDIP = Button((255, 255, 255), 30, 435, 240, 30, text="DIP 2022-PAO2", sizeText=15)
        self.__btnDevelopers = Button((255, 255, 255), 340, 435, 270, 30, text="Beltran - Ochoa", sizeText=15)

        # Initialize images
        self.__imgLogo = pygame.image.load('./imgs/Flappy_Logo.png').convert_alpha()
        self.__imgLogo = pygame.transform.scale(self.__imgLogo, (400, 100))

        self.__imgBird = pygame.image.load('./imgs/bird_sprite.png').convert_alpha()
        self.__imgBird = pygame.transform.scale(self.__imgBird, (75, 50))

        self.__imgBackground = pygame.image.load('./imgs/background.jpg')
        self.__imgBackground = pygame.transform.scale(self.__imgBackground, (CENTER_WIDTH*2, CENTER_HEIGHT*2))