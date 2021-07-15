import pygame
import random

def main():

    pygame.font.init()
    letters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    newColor = False
    
    colorcode = "#"
    for i in range(0, 6):
        rand = random.randint(0, 15)
        colorcode += letters[rand]
    bgcolor = hex_to_rgb(colorcode)

    font_obj = pygame.font.SysFont("comicsansms", 45)

    (width, height) = (300, 500)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Random Color Generator')
    screen.fill(bgcolor)

    text_obj=font_obj.render(colorcode,True,(255, 255, 255))
    screen.blit(text_obj, (22,0))

    pygame.display.flip()

    surf = pygame.image.load("bitmap.png")
    pygame.display.set_icon(surf)
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
            colorcode = "#"
            for i in range(0, 6):
                    rand = random.randint(0, 15)
                    colorcode += letters[rand]
            bgcolor = hex_to_rgb(colorcode)
            print(bgcolor)
            screen.fill(bgcolor)
            text_obj=font_obj.render(colorcode,True,(255, 255, 255))
            screen.blit(text_obj, (22,0))
            pygame.display.update()
            newColor = False


def hex_to_rgb(value):
    value = value.lstrip('#')
    lengthVal = len(value)
    return tuple(int(value[i:i + lengthVal // 3], 16) for i in range(0, lengthVal,lengthVal // 3))


main()
