import sys, time, random, pygame
from collections import deque
import cv2 as cv, mediapipe as mp
from components.Text import Text
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
pygame.init()

# Initialize required elements/environment
VID_CAP = cv.VideoCapture(0)
window_size = (VID_CAP.get(cv.CAP_PROP_FRAME_WIDTH), VID_CAP.get(cv.CAP_PROP_FRAME_HEIGHT)) # width by height
screen = pygame.display.set_mode(window_size)

def pipe_random_height():
    pipe_h = [random.randint(100, (screen.get_height()/2) - 20),random.randint( (screen.get_height()/2)+20, screen.get_height())]
    return pipe_h    

# Bird and pipe
bird_img = pygame.image.load("bird_sprite.png")
bird_img = pygame.transform.scale(bird_img, (bird_img.get_width() / 6, bird_img.get_height() / 6))
bird_frame = bird_img.get_rect()
bird_frame.center = (window_size[0] // 6, window_size[1] // 2)

pipe_img = pygame.image.load("pipe_sprite_single.png")
pipe_img = pygame.transform.rotate(pipe_img, 180)
pipe_img_rotate = pygame.transform.rotate(pipe_img, 180)

pipe_img_rotate = pygame.transform.scale(pipe_img_rotate, (50, screen.get_height()))
pipe_bottom = pipe_img_rotate.get_rect()
pipe_bottom.x = 500
pipe_bottom.y = screen.get_height()/2 + 50 

pipe_img = pygame.transform.scale(pipe_img, (50,screen.get_height()))
pipe_top = pipe_img.get_rect()
pipe_top.x = 500
pipe_top.y = pipe_bottom.y - pipe_bottom.height - 100    

speed = 5
score = 0

game_is_running = True

with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
    while True:
        # Check if game is running
        if not game_is_running:
            text = pygame.font.SysFont("Helvetica Bold.ttf", 64).render('Game over!', True, (99, 245, 255))
            tr = text.get_rect()
            tr.center = (window_size[0]/2, window_size[1]/2)
            screen.blit(text, tr)
            pygame.display.update()
            pygame.time.wait(2000)
            VID_CAP.release()
            cv.destroyAllWindows()
            pygame.quit()
            sys.exit()

        # Check if user quit window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                VID_CAP.release()
                cv.destroyAllWindows()
                pygame.quit()
                sys.exit()

        # Get frame
        ret, frame = VID_CAP.read()
        if not ret:
            print("Empty frame, continuing...")
            continue

        # Clear screen
        screen.fill((125, 220, 232))

        # Face mesh
        frame.flags.writeable = False
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) #OpenCV
        results = face_mesh.process(frame) #MediaPipe
        frame.flags.writeable = True

        # Draw mesh
        if results.multi_face_landmarks and len(results.multi_face_landmarks) > 0:
            # 94 = Tip of nose
            marker = results.multi_face_landmarks[0].landmark[94].y
            bird_frame.centery = (marker - 0.5) * 1.5 * window_size[1] + window_size[1]/2
            if bird_frame.top < 0: bird_frame.y = 0
            if bird_frame.bottom > window_size[1]: bird_frame.y = window_size[1] - bird_frame.height

        # Mirror frame, swap axes because opencv != pygame
        frame = cv.flip(frame, 1).swapaxes(0, 1)

        # Update screen
        pygame.display.set_caption('Flappy Bird: Proyecto PDI - Beltrán, Ochoa')
        pygame.surfarray.blit_array(screen, frame)

        #Movimiento Pipes
        pipe_top.x -= speed
        pipe_bottom.x -= speed

        #Insercio de objetos
        screen.blit(bird_img, bird_frame) #Colocar Bird en la ventana
        screen.blit(pipe_img, pipe_top) #Colocar Bird en la ventana        
        screen.blit(pipe_img_rotate, pipe_bottom) #Colocar Bird en la ventana
        
        txt_score = Text((255,255,255), 100, 30,text="Puntaje " + str(score))
        txt_score.draw(screen)

        if score == 5:
            speed += 1


        if pipe_top.x == 10:
            pipe_bottom.x = 500
            pipe_top.x = 500
            score += 1
            h_b = random.randint(100, screen.get_height() - 50)
            pipe_bottom.y = h_b 
            ht = h_b - pipe_bottom.height - 100
            pipe_top.y = ht
        
        if(bird_frame.colliderect(pipe_top) or bird_frame.colliderect(pipe_bottom)):
            game_is_running = False


        pygame.display.flip()