import pygame
from pygame.locals import *

import cv2 as cv
from views.init import InitView

# Inicializa componentes de Pygame
pygame.init()

# Ajusta el tamaño de la pantalla de Juego
VID_CAP = cv.VideoCapture(0)
window_size = (VID_CAP.get(cv.CAP_PROP_FRAME_WIDTH), VID_CAP.get(cv.CAP_PROP_FRAME_HEIGHT))

# Muestra pantalla inicial
initView = InitView(window_size)
initView.show()