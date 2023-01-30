import pygame

class Text():
    def __init__(self, color, x, y, text = '', sizeText = 20):
        self.color = color
        self.x = x
        self.y = y
        self.text = text
        self.sizeText = sizeText

    def draw(self, screen):
        if self.text != '':
            font = pygame.font.Font('./resources/ARCADE_N.ttf', self.sizeText)
            text = font.render(self.text, 1, self.color)
            screen.blit(text, (self.x - text.get_width()/2, self.y - text.get_height()/2))

    def changeText(self, newText):
        self.text = newText