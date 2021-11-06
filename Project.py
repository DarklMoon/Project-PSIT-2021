import pygame, sys

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE')

#define variable
clicked = False

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



#mainloop
def main():
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

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
