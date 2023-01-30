import pygame
from components.Button import Button
from components.Text import Text

class CreditsView():
    def __init__(self, screen):
        self.screen = screen

        # Buttons/Text/Rectangles
        self.__btnVolver = None
        self.__recPanel = None
        self.__txtCreditos = None

        # Images
        self.__imgBackground = None

        self.__initializeComponents()

    def show(self):
        self.draw()

    def draw(self):
        # Fill the background with cian
        self.screen.fill((0, 199, 218))
        self.screen.blit(self.__imgBackground, (0, 0))

        # Place buttons/texts
        self.__btnVolver.draw(self.screen)
        self.__recPanel.draw(self.screen)
        self.__txtCreditos.draw(self.screen)

    def __btnVolver_Click(self):
        with open("config.txt", 'w') as f:
            f.write('0')
        f.close()

    # Initialize interface's components
    def __initializeComponents(self):
        CENTER_WIDTH, CENTER_HEIGHT = self.screen.get_rect().center
        y = CENTER_HEIGHT + int(CENTER_HEIGHT*5/8)
        self.__btnVolver = Button((118, 191, 20), 250, y, 150, 50, text="Volver",
                                 onClickFunction=self.__btnVolver_Click)
        self.__recPanel = Button((255,255,255), 70, int(CENTER_HEIGHT/3), 500, 275, text="", sizeText=5)
        self.__txtCreditos = Text((0,0,0), CENTER_WIDTH, int(CENTER_HEIGHT/5), text="Creditos", sizeText=25)

        self.__imgBackground = pygame.image.load('./imgs/background.jpg')
        self.__imgBackground = pygame.transform.scale(self.__imgBackground, (CENTER_WIDTH * 2, CENTER_HEIGHT * 2))


