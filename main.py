import pygame
from pygame.locals import *

import cv2 as cv
import sys
from views.init import InitView

# Inicializa componentes de Pygame
pygame.init()
pygame.display.set_caption('Flappy Bird: Proyecto DPI - Beltrán, Ochoa')

# Ajusta el tamaño de la pantalla de Juego
VID_CAP = cv.VideoCapture(0)
window_size = (VID_CAP.get(cv.CAP_PROP_FRAME_WIDTH), VID_CAP.get(cv.CAP_PROP_FRAME_HEIGHT))
screen = pygame.display.set_mode(window_size)

game_is_running = True
initView = InitView(screen)

while True:
    # Check if game is running
    if not game_is_running:
        VID_CAP.release()
        cv.destroyAllWindows()
        pygame.quit()
        sys.exit()

    # Check if user quit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
            VID_CAP.release()
            cv.destroyAllWindows()
            pygame.quit()
            sys.exit()

    initView.show()