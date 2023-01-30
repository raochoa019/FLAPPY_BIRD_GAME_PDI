import pygame
import cv2 as cv
import sys
from views.init import InitView
from views.credits import CreditsView
from views.game import GameView
from pygame import mixer

state = 0

# Inicializa componentes de Pygame
pygame.init()
pygame.display.set_caption('Flappy Bird: Proyecto DPI - Beltrán, Ochoa')

mixer.init()
mixer.music.load("./resources/back_music.mp3")
mixer.music.play()

# Ajusta el tamaño de la pantalla de Juego
VID_CAP = cv.VideoCapture(0)
window_size = (VID_CAP.get(cv.CAP_PROP_FRAME_WIDTH), VID_CAP.get(cv.CAP_PROP_FRAME_HEIGHT))
screen = pygame.display.set_mode(window_size)

game_is_running = True
initView = InitView(screen)
creditsView = CreditsView(screen)
gameView = GameView(screen, VID_CAP, window_size)

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
            mixer.music.stop()
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
        initView.show()     # Vista Inicial
    elif state == 1:
        creditsView.show()  # Vista Créditos
    elif state == 2:
        gameView.show()     # Vista Juego
    else:
        gameView.show()     # Vista GameOver
        game_is_running = False

    pygame.display.update()