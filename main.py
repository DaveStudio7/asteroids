import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    font = pygame.font.Font(None, 32)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        for thing in drawable:
            thing.draw(screen)

        score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        lives_text = font.render(f"Lives: {player.lives}", True, (255, 255, 255))
        screen.blit(lives_text, (10, 40))

        pygame.display.flip()
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.split()
                    shot.kill()
                    player.score += 10

        for asteroid in asteroids:
            if asteroid.collisions(player) and player.invulnerable_timer <= 0:
                player.lives -= 1
                if player.lives > 0:
                    player.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    player.velocity = pygame.Vector2(0, 0)
                    player.invulnerable_timer = 2
                else:
                    print("Game over!")
                    sys.exit()
        
        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()