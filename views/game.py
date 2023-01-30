import sys, random, pygame
import cv2 as cv, mediapipe as mp
from components.Text import Text

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

class GameView():
    def __init__(self, screen, video, window_size):
        self.screen = screen
        self.VID_CAP = video
        self.window_size = window_size
        self.speed = 5
        self.score = 0
        self.previous_score = -1
        self.__needUpdateVelocity = False

        # Components
        self.__bird_img = None
        self.__pipe_img = None
        self.__pipe_img_rotate = None

        self.__bird_frame = None
        self.__pipe_bottom = None
        self.__pipe_top = None

        self.__txt_score = None
        self.__initializeComponents()

    def show(self):
        self.draw()

    def draw(self):
        with mp_face_mesh.FaceMesh(
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as face_mesh:

            x = ''
            with open("config.txt") as f:
                x = f.read(1)
            f.close()

            state = int(x)
            if state == 4: # Game Over
                CENTER_WIDTH, CENTER_HEIGHT = self.screen.get_rect().center
                txtGameOver = Text((99, 245, 255), CENTER_WIDTH, CENTER_HEIGHT, text="Game Over", sizeText=64)
                txtGameOver.draw(self.screen)
                pygame.display.update()
                pygame.time.wait(3000)
            else:
                # Get frame
                ret, frame = self.VID_CAP.read()

                # Clear screen
                self.screen.fill((125, 220, 232))

                # Face mesh
                frame.flags.writeable = False
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # OpenCV
                results = face_mesh.process(frame)  # MediaPipe
                frame.flags.writeable = True

                # Draw mesh
                if results.multi_face_landmarks and len(results.multi_face_landmarks) > 0:
                    # 94 = Tip of nose
                    marker = results.multi_face_landmarks[0].landmark[94].y
                    self.__bird_frame.centery = (marker - 0.5) * 1.5 * self.window_size[1] + self.window_size[1] / 2
                    if self.__bird_frame.top < 0: self.__bird_frame.y = 0
                    if self.__bird_frame.bottom > self.window_size[1]: self.__bird_frame.y = self.window_size[1] - self.__bird_frame.height

                # Mirror frame, swap axes because opencv != pygame
                frame = cv.flip(frame, 1).swapaxes(0, 1)

                # Update screen
                pygame.surfarray.blit_array(self.screen, frame)
                self.__placeComponents()

                # Movimiento Pipes
                self.__pipe_top.x -= self.speed
                self.__pipe_bottom.x -= self.speed

                # if (self.score % 3 == 0) and self.__needUpdateVelocity:
                #     print("Actualiza velocidad")
                #     self.__needUpdateVelocity = False
                #     self.speed += 2
                # 
                # if self.previous_score % 3 == 0:
                #     self.__needUpdateVelocity = True

                if self.__pipe_top.x == 10:
                    self.__pipe_bottom.x = self.window_size[0]
                    self.__pipe_top.x = self.window_size[0]
                    self.score += 1
                    self.__txt_score.changeText("Puntaje: " + str(self.score))
                    self.previous_score += 1
                    h_b = random.randint(100, self.screen.get_height() - 50)
                    self.__pipe_bottom.y = h_b
                    ht = h_b - self.__pipe_bottom.height - 100
                    self.__pipe_top.y = ht

                if (self.__bird_frame.colliderect(self.__pipe_top) or self.__bird_frame.colliderect(self.__pipe_bottom)):
                    with open("config.txt", 'w') as f:
                        f.write('4')
                    f.close()

    def __placeComponents(self):
        # Insercion de objetos
        self.screen.blit(self.__bird_img, self.__bird_frame)  # Colocar Bird en la ventana
        self.screen.blit(self.__pipe_img, self.__pipe_top)  # Colocar Bird en la ventana
        self.screen.blit(self.__pipe_img_rotate, self.__pipe_bottom)  # Colocar Bird en la ventana
        self.__txt_score.draw(self.screen)

    def __initializeComponents(self):
        # Imagen Personaje
        self.__bird_img = pygame.image.load("./imgs/bird_sprite.png")
        self.__bird_img = pygame.transform.scale(self.__bird_img, (self.__bird_img.get_width() / 6, self.__bird_img.get_height() / 6))
        self.__bird_frame = self.__bird_img.get_rect()
        self.__bird_frame.center = (self.window_size[0] // 6, self.window_size[1] // 2)

        # Imagen Pipes
        self.__pipe_img = pygame.image.load("./imgs/pipe_sprite_single.png")
        self.__pipe_img = pygame.transform.rotate(self.__pipe_img, 180)
        self.__pipe_img_rotate = pygame.transform.rotate(self.__pipe_img, 180)
        self.__pipe_img_rotate = pygame.transform.scale(self.__pipe_img_rotate, (50, self.screen.get_height()))

        self.__pipe_bottom = self.__pipe_img_rotate.get_rect()
        self.__pipe_bottom.x = 500
        self.__pipe_bottom.y = self.screen.get_height() / 2 + 50

        self.__pipe_img = pygame.transform.scale(self.__pipe_img, (50, self.screen.get_height()))
        self.__pipe_top = self.__pipe_img.get_rect()
        self.__pipe_top.x = 500
        self.__pipe_top.y = self.__pipe_bottom.y - self.__pipe_bottom.height - 100

        self.__txt_score = Text((255, 255, 255), 120, 30, text="Puntaje: " + str(self.score))