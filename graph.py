import pygame, time

from dataFile import data

class DrawHeatMap:
    # Create the screen
    screen = pygame.display.set_mode((800,800))

    # Colours
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    def __init__(self, data):
        pygame.init()

        self.data = data

        self.drawGraph()
        self.drawData()

        # Output the display
        pygame.display.flip()

    def drawGraph(self):
        screen = self.screen

        # Set the screen white
        pygame.draw.rect(screen, self.WHITE, (0, 0, 800, 800))

        # Draw the graph lines
        pygame.draw.line(screen, self.BLACK, (25, 25), (25, 780), 5)
        pygame.draw.line(screen, self.BLACK, (780, 780), (25, 780), 5)

        # Draw the scale
        for x in range(1, 16):
            self.drawText(x, x * 50, 785)
        for y in range(1, 16):
            # Align the text right
            if y < 10:
                x = 15
            else:
                x = 10
            self.drawText(y, x, (y * -50) + 800)

    def drawData(self):
        for x in range(50, 800):
            for y in range(50, 800):
                x1, y1 = self.translate(x, y)

                maxSplit = x / 50
                maxTermLen = y / 50

                percent = self.data[maxSplit][maxTermLen]

                self.drawPix(x1, y1, self.getColour(percent))

    def drawText(self, text, x, y, size = 10, color = BLACK, fontType = 'arial.ttf'):
        text = str(text)
        font = pygame.font.Font(fontType, size)
        text = font.render(text, True, color)
        self.screen.blit(text, (x, y))

    # Translate the pixel to the correct screen location
    def translate(self, x, y):
        x -= 20
        y *= -1
        y += 825
        return x, y

    def drawPix(self, x, y, colour):
        self.screen.set_at((x, y), colour)

    # Dodgy function (optimised for the data)
    def getColour(self, val):
        val *= 1000
        if val < 100:
            g = int(val / 100.0 * 255)
            r = 75 - int(val / 100.0 * 50 )
            return (r,g,255)
        elif val < 250:
            val -= 100
            b = 255 - (val / 150.0 * 230)
            return (25,255,b)
        elif val < 400:
            val -= 250
            r = (val / 150.0 * 230) + 25
            return (r,255,25)
        elif val < 600:
            val -= 400
            g = 255 - (val / 200.0 * 255)
            return (255, g, 25)
        return (0,0,0)

d = DrawHeatMap(data)
time.sleep(10)
