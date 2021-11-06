import pygame, sys

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE')

#define variable
markers = []
clicked = False
positon = []
player = 1
#color
LIGHT_GREY = (192, 192, 192)
DARK_GREY = (96, 96, 96)

FPS = 60

def draw_board():
    BG_COLOR = (102, 178, 255)
    LIGHT_PURPLE = (51, 153, 255)
    screen.fill( BG_COLOR )
    #Vertical
    pygame.draw.line( screen, LIGHT_PURPLE, (200, 0), (200, 600), 20) #1
    pygame.draw.line( screen, LIGHT_PURPLE, (400, 0), (400, 600), 20) #2
    #Horizontal
    pygame.draw.line( screen, LIGHT_PURPLE, (0, 200), (600, 200), 20) #1
    pygame.draw.line( screen, LIGHT_PURPLE, (0, 400), (600, 400), 20) #2

for x in range(3):
    row = [0]*3
    markers.append(row)

def draw_markers():
    x_pos = 0
    for x in markers:
        o_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, LIGHT_GREY, (x_pos * 200 + 115), (x_pos * 200 + 185))
                pygame.draw.line(screen, LIGHT_GREY, (x_pos * 200 + 185), (x_pos * 200 + 115))
            if y == 0:
                pygame.draw.circle(screen, DARK_GREY, (x_pos * 200 + 100), 100, 6)

#mainloop
    clock = pygame.time.Clock()
    run = True
    while run:
        draw_board()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                position = pygame.mouse.get_position()
                mark_x = position[0]
                mark_y = position[1]
                if markers[mark_x // 200][mark_y // 200] == 0:
                    markers[mark_x // 200][mark_y // 200] = player
                    player *= -1



        pygame.display.update()
    pygame.quit()

if __name__ == "__main__"
