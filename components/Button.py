import pygame

class Button():
    def __init__(self, color, x, y, width, height, text = '', sizeText = 20, onClickFunction=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.sizeText = sizeText
        self.onClickFunction = onClickFunction


    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0, 10)
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 2, 10)

        if self.text != '':
            font = pygame.font.Font('./resources/ARCADE_N.ttf', self.sizeText)
            #font = pygame.font.SysFont('Arial', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))


    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False