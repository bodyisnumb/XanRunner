import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

block_color = (255,255,255,128)

seva_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Run away lil Seva!')
clock = pygame.time.Clock()

SevaImg = pygame.image.load('Images/sevaface.png')
XanImg = pygame.image.load('Images/xanbar.png')
AcidTrip = pygame.image.load('Images/acid-trip.jpg')
OverdoseSound = pygame.mixer.Sound('Music/overdose.wav')
pygame.mixer.music.load('Music/bg_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Ovedoses Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.ellipse(gameDisplay, color, [thingx, thingy, thingw, thingh])
    gameDisplay.blit(XanImg, [thingx, thingy, thingw, thingh])


def seva(x, y):
    gameDisplay.blit(SevaImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    pygame.mixer.Sound.play(OverdoseSound)
    pygame.mixer.music.pause()
    pygame.mixer.music.unpause()
    message_display('You Overdosed')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 80
    thing_height = 90

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
       # gameDisplay.fill(white)
        gameDisplay.blit(AcidTrip, (0, 0))

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        seva(x, y)
        things_dodged(dodged)

        if x > display_width - seva_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + seva_width > thing_startx and x + seva_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()

