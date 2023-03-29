import pygame

no_of_clients=0
width = 1000
height = 1000
window_size = pygame.display.set_mode((width, height))
pygame.display.set_caption("Player")


def display_window():
    window_size.fill((255,255,255))
    pygame.display.update()

def main():
    game_loop=True
    pygame.init()
    while game_loop:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                game_loop = False
                pygame.quit()
        display_window()

main()
