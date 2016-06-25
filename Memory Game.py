import pygame as py
import random
import time

py.init()
FPS = 30
display_width = 800
display_height = 600
gameDisplay = py.display.set_mode((display_width, display_height))
py.display.set_caption('Memory Game')
clock = py.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
blue = (122, 94, 255)

imgArray = []

img1 = py.image.load("1.jpg")
imgArray.append(img1)
img2 = py.image.load("2.jpg")
imgArray.append(img2)
img3 = py.image.load("3.jpg")
imgArray.append(img3)
img4 = py.image.load("4.jpg")
imgArray.append(img4)
img5 = py.image.load("5.jpg")
imgArray.append(img5)
img6 = py.image.load("6.jpg")
imgArray.append(img6)
img7 = py.image.load("7.jpg")
imgArray.append(img7)
img8 = py.image.load("8.jpg")
imgArray.append(img8)
img9 = py.image.load("9.jpg")
imgArray.append(img9)
img10 = py.image.load("10.jpg")
imgArray.append(img10)

random.shuffle(imgArray)

class Card():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.card_size = 100
        self.isFaceUp = False
    def isClicked(self, pos):
        if py.mouse.get_pos()[0] > self.x and py.mouse.get_pos()[0] < self.x + self.card_size:
            if py.mouse.get_pos()[1] > self.y and py.mouse.get_pos()[1] < self.y + self.card_size:
                return True
    def draw(self):
        py.draw.rect(gameDisplay, black, [self.x, self.y, self.card_size, self.card_size])
        py.draw.rect(gameDisplay, blue, [self.x - 1, self.y - 1, self.card_size - 1, self.card_size - 1])
        self.isFaceUp = False
    def flip(self):
        gameDisplay.blit(self.img, (self.x, self.y))
        self.isFaceUp = True
                                   
        
cards = []

selected = []
for i in range(8):
    randomInd = random.randint(0, len(imgArray) - 1)
    image = imgArray[randomInd]
    selected.append(image)
    selected.append(image)
    del imgArray[randomInd]
random.shuffle(selected)

for x in range(4):
    for y in range(4):
            cards.append(Card(y * 100, x * 100, selected.pop()))
random.shuffle(cards)
    
def win():
    gameDisplay.fill(black)
    message_display("You Win!")
    time.sleep(2)
    py.quit()
    quit()
    
def message_display(text):
    largeText = py.font.SysFont('verdana',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    py.display.update()
    time.sleep(2)
    gameLoop()
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def check_win():
    for card in cards:
        if not(card.isFaceUp):
           return False
    return True

def gameLoop():
    flipped = []
    numFlipped = 0

    for card in cards:
        card.draw()
        
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
            if event.type == py.MOUSEBUTTONUP:
                pos = py.mouse.get_pos()
                for card in cards:
                    if card.isClicked(pos) and not(card.isFaceUp):
                        flipped.append(card)
                        card.flip()
                        py.display.update()
                        break
        if (check_win()):
            break
        if len(flipped) == 2:
            if flipped[0].img == flipped[1].img:
                flipped[0].flip()
                flipped[1].flip()
            else:
                time.sleep(0.5)
                flipped[0].draw()
                flipped[1].draw()
            flipped = []
        elif len(flipped) == 1:
            flipped[0].flip()
        py.display.update()
        clock.tick(FPS)
gameLoop()
win()

