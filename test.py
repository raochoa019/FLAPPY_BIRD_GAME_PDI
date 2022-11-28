import sys, time, random, pygame
from collections import deque
import cv2 as cv, mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
pygame.init()

VID_CAP = cv.VideoCapture(0)
window_size = (VID_CAP.get(cv.CAP_PROP_FRAME_WIDTH), VID_CAP.get(cv.CAP_PROP_FRAME_HEIGHT)) # width by height
screen = pygame.display.set_mode(window_size)

with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:

    while True:
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

        screen.fill((125, 220, 232))

        # Face mesh
        frame.flags.writeable = False
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) #OpenCV
        results = face_mesh.process(frame) #MediaPipe
        frame.flags.writeable = True

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(image=frame,
                                          landmark_list=face_landmarks,
                                          connections=mp_face_mesh.FACEMESH_TESSELATION,
                                          landmark_drawing_spec=None,
                                          connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
                mp_drawing.draw_landmarks(image=frame,
                                          landmark_list=face_landmarks,
                                          connections=mp_face_mesh.FACEMESH_CONTOURS,
                                          landmark_drawing_spec=None,
                                          connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
                mp_drawing.draw_landmarks(image=frame,
                                          landmark_list=face_landmarks,
                                          connections=mp_face_mesh.FACEMESH_IRISES,
                                          landmark_drawing_spec=None,
                                          connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style())
        frame = cv.flip(frame, 1).swapaxes(0, 1)
        pygame.display.set_caption('Flappy Bird: Proyecto PDI - Beltrán, Ochoa')
        pygame.surfarray.blit_array(screen, frame)
        
        pygame.display.flip()

