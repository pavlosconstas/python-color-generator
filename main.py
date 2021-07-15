import pygame
import random

letters = ["1", "2", "3", "4", "5", "6", "7",
           "8", "9", "0", "a", "b", "c", "d", "e", "f"]


def main():
    surf = pygame.image.load("bitmap.png")
    pygame.display.set_icon(surf)
    
    newColor = False
    colorcode = genColor(letters)
    bgcolor = hex_to_rgb(colorcode)
    

    screen = pygame.display.set_mode((300, 500))
    pygame.display.set_caption('Random Color Generator')
    screen.fill(bgcolor)

    pygame.font.init()
    font_obj = pygame.font.SysFont("comicsansms", 45)
    text_obj = font_obj.render(colorcode, True, (255, 255, 255))
    screen.blit(text_obj, (22, 0))

    pygame.display.flip()

    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    newColor = True
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_RETURN:
                    newColor = True

        while(newColor):
            colorcode = genColor(letters)
            bgcolor = hex_to_rgb(colorcode)
            print(bgcolor)
            screen.fill(bgcolor)
            text_obj = font_obj.render(colorcode, True, (255, 255, 255))
            screen.blit(text_obj, (22, 0))
            pygame.display.update()
            newColor = False


def genColor(letters):
    colorcode = "#"
    for i in range(0, 6):
        rand = random.randint(0, 15)
        colorcode += letters[rand]
    return colorcode


def hex_to_rgb(value):
    value = value.lstrip('#')
    lengthVal = len(value)
    return tuple(int(value[i:i + lengthVal // 3], 16) for i in range(0, lengthVal, lengthVal // 3))


main()
