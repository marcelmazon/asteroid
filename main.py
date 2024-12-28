import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # color = pygame.Color(255, 0, 0)
    clock = pygame.time.Clock()
    dt = 0

    #player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shootable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shootable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # MAIN GAME LOOP
    while (True):
        for event in pygame.event.get(): # Makes window's close button work
            if event.type == pygame.QUIT:
                return


        screen.fill((0,0,0))

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for shot in shootable:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()

        for item in drawable:    
            item.draw(screen)

        
        pygame.display.flip()

        milisecs = clock.tick(60) 
        # So that less CPU resources
        # pauses game loop for 1/60 of second
        
        dt = milisecs / 1000



    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
