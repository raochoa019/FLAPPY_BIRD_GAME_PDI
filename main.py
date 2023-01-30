import pygame
import cv2 as cv
import sys
from views.init import InitView
from views.credits import CreditsView

state = 0

# Inicializa componentes de Pygame
pygame.init()
pygame.display.set_caption('Flappy Bird: Proyecto DPI - Beltrán, Ochoa')

# Ajusta el tamaño de la pantalla de Juego
VID_CAP = cv.VideoCapture(0)
window_size = (VID_CAP.get(cv.CAP_PROP_FRAME_WIDTH), VID_CAP.get(cv.CAP_PROP_FRAME_HEIGHT))
print(window_size)
screen = pygame.display.set_mode(window_size)

game_is_running = True
initView = InitView(screen)
creditsView = CreditsView(screen)

while True:
    # Check if game is running
    if not game_is_running:
        VID_CAP.release()
        cv.destroyAllWindows()
        with open("config.txt", 'w') as f:
            f.write('0')
        f.close()
        pygame.quit()
        sys.exit()

    # Check if user quit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
            VID_CAP.release()
            cv.destroyAllWindows()
            with open("config.txt", 'w') as f:
                f.write('0')
            f.close()
            pygame.quit()
            sys.exit()

    x=''
    with open("config.txt") as f:
        x = f.read(1)
    f.close()

    state = int(x)
    if state == 0:
        initView.show()
    elif state == 1:
        creditsView.show()
    elif state == 2:
        pass # game.show()
    else:
        pass # game.show()

    pygame.display.update()