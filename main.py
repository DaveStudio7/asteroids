import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        updatable.update(dt)
        
        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()